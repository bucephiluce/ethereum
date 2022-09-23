import os
# 设置环境变量必须放在第一行
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2" 

import tensorflow as tf
import glob
import pandas as pd
import re
import numpy as np

v1 = tf.compat.v1
# 保证session.run()能够正常运行
v1.disable_eager_execution()

def read_pic():
    """
    读取图片数据
    流程分析: 
    # 1) 构造文件名队列
    # 2) 读取与解码
    # 3) 批处理
    """
    # 1) 构造文件名队列 
    # 获取文件名列表
    file_names = glob.glob('./GenPics/*.jpg')
    file_queue = v1.train.string_input_producer(file_names)

    # 2) 读取与解码
    # 读取
    reader = v1.WholeFileReader()
    file_name, image = reader.read(file_queue)
    # 解码
    decoded = v1.image.decode_jpeg(image)
    # 更新形状
    decoded.set_shape([20,80,3])
    # 更新类型
    image_cast = v1.cast(decoded, v1.float32)

    # 3) 批处理
    filename_batch, image_batch = v1.train.batch([file_name, image_cast], batch_size=100, num_threads=2, capacity=200)

    return filename_batch, image_batch

def parse_csv():
    # 解析csv文件
    data = pd.read_csv('./GenPics/labels.csv',names=['file_num', 'chars'], index_col='file_num')
    # 将标签值NZPP->[13, 25, 15, 15]
    labels = []
    for label in data['chars']:
        letters = []
        for letter in label:
            # 将字母转换成ASC2码
            letters.append(ord(letter) - ord('A'))
        labels.append(letters)
    data['labels'] = labels

    return data

def filename2label(filenames, csv_data):
    """
    将filename和标签值联系起来
    :param filenames:
    :param csv_data:
    :return:
    """
    labels = []
    for filename in filenames :
        file_num = re.findall(r'\d+',str(filename))[0]
        label = csv_data.loc[int(file_num), 'labels']
        labels.append(label)
    return np.array(labels)

def create_variable(shape):
    # 定义权重和偏置  stddev 标准差
    return v1.Variable(initial_value=v1.random_normal(shape=shape,stddev=0.01))
    # return v1.Variable(initial_value=v1.random_normal(shape=shape,mean=0,stddev=1))

def cnn_model(x):
    """
    构造卷积神经网络
    流程分析: 
    # 1) 第一个卷积大层
        # 1. 卷积层 filter
        # 2. 激活层
        # 3. 池化层 subsample
    # 2) 第二个卷积大层
        # 1. 卷积层 filter
        # 2. 激活层
        # 3. 池化层 subsample
    # 3) 全连接层
    
    """
    # 1) 第一个卷积大层
    with v1.variable_scope('conv1'):
        # 1. 卷积层 filter
        # 定义filter和偏置 
        # [None, 20, 80, 3]
        conv1_weights = create_variable(shape=[5,5,3,32])
        conv1_bias = create_variable(shape=[32])
        conv1_x = v1.nn.conv2d(input=x, filter=conv1_weights, strides=[1,1,1,1], padding='SAME') + conv1_bias

        # 2. 激活层
        relu1_x = v1.nn.relu(conv1_x)

        # 3. 池化层 subsample 窗口: 2*2 ; 步长: 2 
        pool1_x = v1.nn.max_pool(value=relu1_x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
        # 输出形状：[None, 10, 40, 32]

    # 2) 第二个卷积大层
    with v1.variable_scope('conv2'):
        # 1. 卷积层 filter
        # 定义filter和偏置 [filter_height, filter_width, in_channels,out_channels]
        conv2_weights = create_variable(shape=[5,5,32,64])
        conv2_bias = create_variable(shape=[64])
        conv2_x = v1.nn.conv2d(input=pool1_x, filter=conv2_weights, strides=[1,1,1,1], padding='SAME') + conv2_bias

        # 2. 激活层
        relu2_x = v1.nn.relu(conv2_x)

        # 3. 池化层 subsample
        pool2_x = v1.nn.max_pool(value=relu2_x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
        # 输出形状：[None, 5, 20, 64]

    # 3) 全连接层
    with v1.variable_scope('full_connection'):
        # 全连接层需要改变形状到二维
        # [None, 5, 20, 64]->[None, 5*20*64]
        # [None, 5*20*64] * [5*20*64, 4*26] = [None, 4*26] 
        # reshape中的shape没有none,需用-1代替
        fc_x = v1.reshape(pool2_x, shape=[-1, 5*20*64])
        fc_weights = create_variable(shape=[5*20*64, 4*26])
        fc_bias = create_variable(shape=[4*26])
        y_predict = v1.matmul(fc_x, fc_weights) + fc_bias
    
    return y_predict

if __name__ == '__main__':
    file_name, image = read_pic()
    csv_data = parse_csv()

    # 1. 准备数据
    x = v1.placeholder(tf.float32, shape=[None, 20, 80, 3])
    y_true = v1.placeholder(tf.float32, shape=[None,4*26])

    # 2. 构造模型
    y_predict = cnn_model(x)

    # 3. 构造损失函数
    loss_list = v1.nn.sigmoid_cross_entropy_with_logits(labels=y_true, logits=y_predict)
    loss = v1.reduce_mean(loss_list)

    # 4. 优化损失
    # optimizer = v1.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)
    optimizer = v1.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

    # 5. 计算准确率
    # 1_ 先进行变形
    y_true_reshape = v1.reshape(y_true, [-1,4,26])
    y_predict_reshape = v1.reshape(y_predict, [-1,4,26])
    # 2_找到最大的位置
    y_true_argmax = v1.argmax(y_true_reshape, axis=2)
    y_predict_argmax = v1.argmax(y_predict_reshape, axis=2)
    # [True,True,True,False]
    equal_list = v1.equal(y_true_argmax,y_predict_argmax)
    # [True,True,True,False]--> False
    result_list = v1.reduce_all(equal_list,axis=1)
    accuracy = v1.reduce_mean(v1.cast(result_list, v1.float32))

    # 初始化变量
    init = v1.global_variables_initializer()

    # 开启线程
    with v1.Session() as sess: 
        # 初始化变量
        sess.run(init)

        # 开启线程
        coord = v1.train.Coordinator()
        threads = v1.train.start_queue_runners(sess=sess, coord=coord)

        for i in range(1000):
            filename_val , image_val = sess.run([file_name, image])
            # [24, 9, 20, 21]
            labels = filename2label(filename_val, csv_data)
            # 将标签值,转换成one-hot编码
            labels_val = v1.reshape(v1.one_hot(labels, depth=26, axis=-1),[-1, 4*26]).eval()
            _, loss_val, accuracy_val = sess.run([optimizer, loss, accuracy], feed_dict={x: image_val, y_true: labels_val})
            print("第%d次训练后损失为%f，准确率为%f" % (i+1, loss_val, accuracy_val))
        
        # 回收线程
        coord.request_stop()
        coord.join(threads)

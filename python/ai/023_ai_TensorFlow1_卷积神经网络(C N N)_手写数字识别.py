import os
# 设置环境变量必须放在第一行
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2" 

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# from tensorflow.contrib.slim.python.slim.nets.inception_v3 import inception_v3_base

v1 = tf.compat.v1
# 保证session.run()能够正常运行
v1.disable_eager_execution()

# 在命令行中需要使用 --model_path --is_train
# eg: python .\022_ai_TensorFlow1_全连接实现_手写数字识别.py --is_train=0
v1.app.flags.DEFINE_string('model_path', 'tmp/modelckpt/fc_nn_model.ckpt', '模型路径+模型名称')
v1.app.flags.DEFINE_integer('is_train', 1, '指定是否是训练模型: 1: 表示进行训练; 0: 表示进行预测')
FLAGS = v1.app.flags.FLAGS

def create_variable(shape):
    # 定义权重和偏置  stddev 标准差
    return v1.Variable(initial_value=v1.random_normal(shape=shape))

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
        # 将x[None, 784]形状进行修改 
        # reshape中的shape没有none,需用-1代替
        input_x = v1.reshape(x, shape=[-1, 28, 28, 1])
        # 定义filter和偏置
        conv1_weights = create_variable(shape=[5,5,1,32])
        conv1_bias = create_variable(shape=[32])
        conv1_x = v1.nn.conv2d(input=input_x, filter=conv1_weights, strides=[1,1,1,1], padding='SAME') + conv1_bias

        # 2. 激活层
        relu1_x = v1.nn.relu(conv1_x)

        # 3. 池化层 subsample 窗口: 2*2 ; 步长: 2 
        pool1_x = v1.nn.max_pool(value=relu1_x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
        # 输出形状：[None, 14, 14, 32]

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
        # 输出形状：[None, 7, 7, 64]

    # 3) 全连接层
    with v1.variable_scope('full_connection'):
        # [None, 7, 7, 64]->[None, 7*7*64]
        # [None, 7*7*64] * [7*7*64, 10] = [None, 10] 
        # reshape中的shape没有none,需用-1代替
        fc_x = v1.reshape(pool2_x, shape=[-1, 7*7*64])
        fc_weights = create_variable(shape=[7*7*64, 10])
        fc_bias = create_variable(shape=[10])
        y_predict = v1.matmul(fc_x, fc_weights) + fc_bias
    
    return y_predict

def full_connection():
    """
    使用全连接来实现手写数字的识别
    流程分析: 
    # 1) 准备数据
    # 2) 构建模型
    # 3) 构造损失函数
    # 4) 优化损失
    
    """
    print('============================开始运行================================')
    # 查看 tensorflow 的版本
    # print('查看 tensorflow 的版本: \n', tf.__version__)
    # 查看自己现在用的环境路径
    # print('查看 tensorflow 的环境路径: \n', tf.__file__)

    # 1) 准备数据
    with v1.variable_scope('prepare_data'):
        mnist = input_data.read_data_sets('mnist_data', one_hot = True)
        # 不清楚提取多少样本数量, 所以使用占位符表示
        x = v1.placeholder(dtype=v1.float32, shape=(None, 784))
        y_true = v1.placeholder(dtype=v1.float32, shape=(None, 10))

    # 2) 构建模型--网络
    y_predict = cnn_model(x)
    
    # 3) 构造损失函数 
    with v1.variable_scope('loss_function'):
        # 3.1 激活函数: softmax 
        # 3.2 计算损失的函数: 交叉熵损失函数cross_entropy 
        # 3.3 输入值: 线性回归函数logits 的输出值 
        # 3.4 返回值: 一个损失值列表
        loss_list = v1.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict)
        # 3.5 计算出一个损失均值
        error = v1.reduce_mean(loss_list)

    # 4) 优化损失
    with v1.variable_scope('optimizer'):
        # 学习率
        # optimizer = v1.train.GradientDescentOptimizer(learning_rate=0.001).minimize(error)
        # 使用亚当优化器
        optimizer = v1.train.AdamOptimizer(learning_rate=0.01).minimize(error)

    # 5、计算准确率 
    with v1.variable_scope('accuracy'):
        # axis=None,//0是纵轴 1是横轴 
        # tf.argmax()计算最大值所在列数
        equal_list = v1.equal(v1.argmax(y_predict,axis = 1),v1.argmax(y_true,axis = 1))
        accuracy = v1.reduce_mean(v1.cast(equal_list,v1.float32))

    # 2_ 收集变量 用于 tensorboard 的可视化
    # 2_1_ 收集标量
    v1.summary.scalar('error', error)
    v1.summary.scalar('accuracy', accuracy)
    # 2_2_ 收集高纬度变量
    # v1.summary.histogram('weights', weights)
    # v1.summary.histogram('bias', bias)
    # 3_合并变量
    merged = v1.summary.merge_all()

    # 实例化模型保存
    saver = v1.train.Saver()

    # 初始化变量
    init = v1.global_variables_initializer()

    # 开启会话
    with v1.Session() as sess : 
        sess.run(init)

        # 加载模型 当存在checkpoint 就加载模型
        # if os.path.exists('tmp/modelckpt/checkpoint'):
        #     saver.restore(sess, FLAGS.model_path)

        # 1_ 创建事件文件 tensorboard可视化
        file_writer = v1.summary.FileWriter(logdir='tmp/summary', graph=sess.graph)

        if FLAGS.is_train == 1:

            # 开始训练
            for i in range(3000):
                step = i+1
                # 获取数据, 实时提供
                # 每次提供 100 个样本
                image, label = mnist.train.next_batch(50)

                _, loss,accuracy_val,summary = sess.run([optimizer, error, accuracy,merged] , feed_dict={x:image, y_true:label})
                print('第{1}次的训练; 损失为: {0}; 准确率为: {2}'.format(loss, step, accuracy_val))
                # 4_运行合并变量操作
                # summary = sess.run(merged)
                # 5_每次迭代之后重新将变量写入事件文件
                file_writer.add_summary(summary,step)

                # 保存模型 checkpoint=ckpt
                # if step % 100 == 0 :
                #     saver.save(sess, FLAGS.model_path)
        else:
            for i in range(100):
                # 每次拿一个样本进行预测
                image, label = mnist.test.next_batch(1)

                y_true_new, y_predict_new = sess.run([y_true, y_predict] , feed_dict={x:image, y_true:label})
                print('第{0}个样本的真实值为: {1}; 模型的预测结果为: {2} '.format(i+1,
                                                                                 v1.argmax(y_true_new,axis = 1).eval(),
                                                                                 v1.argmax(y_predict_new,axis = 1).eval()
                                                                                ))

    print('============================结束运行================================')

    return None

if __name__ == '__main__':
    full_connection()

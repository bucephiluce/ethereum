import os
# 设置环境变量必须放在第一行
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2" 

import tensorflow as tf

v1 = tf.compat.v1
# 保证session.run()能够正常运行
v1.disable_eager_execution()

def picture_read(file_list):
    """
    狗图片读取案例
    流程分析: 
    # 1) 构造文件名队列
    # 2) 读取与解码
    # 3) 设置图片统一格式
    # 4) 批处理图片
    # 5) 使用队列必须开启线程
    6) WholeFileReader.__init__  replaced by `tf.data`. Use `tf.data.Dataset.map(tf.read_file)`. 
    
    """
    print('============================开始运行================================')
    # 1) 构造文件名队列 文件名 = 文件名 + 路径
    file_queue = v1.train.string_input_producer(file_list)

    # 2) 读取与解码
    # 读取阶段
    reader = v1.WholeFileReader()
    # key: 文件名 ; value: 一张图片的原始编码
    key, value = reader.read(file_queue)
    print('key: \n', key)
    print('value: \n', value)
    # 解码阶段
    image = v1.image.decode_jpeg(value)
    print('image: \n', image)

    # 3) 设置图片统一格式, 并且修改类型
    image_resize = v1.image.resize_images(image, [224,224])
    print('image_resize: \n', image_resize)

    image_resize.set_shape([224,224,3])
    print('image_resize: \n', image_resize)

    # 4) 批处理图片  replaced by `tf.data`. Use `tf.data.Dataset.batch(batch_size)` (or `padded_batch(...)`
    image_batch = v1.train.batch([image_resize], batch_size=100, num_threads=1, capacity=100)
    print('image_batch: \n', image_batch)

    # 开启会话
    with v1.Session() as sess:
        # 开启线程
        # 实例化一个线程协调员
        coord = v1.train.Coordinator()
        threads = v1.train.start_queue_runners(sess=sess, coord=coord)

        key_new, value_new, image_new, image_resize_new, image_batch_new = sess.run([key, value, image, image_resize, image_batch])
        print('key_new: \n', key_new)
        print('value_new: \n', value_new)
        print('image_new: \n', image_new)
        print('image_resize_new: \n', image_resize_new)
        print('image_batch_new: \n', image_batch_new)

        # 回收线程
        coord.request_stop()
        coord.join(threads=threads)


    print('============================结束运行================================')

if __name__ == '__main__':

    # 构造文件名
    file_names = os.listdir('./dog')
    # 文件 = 文件名 + 路径
    file_list = [os.path.join('./dog/', file) for file in file_names]
    picture_read(file_list)
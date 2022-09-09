import os
# 设置环境变量必须放在第一行
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2" 

import tensorflow as tf

v1 = tf.compat.v1
# 保证session.run()能够正常运行
v1.disable_eager_execution()

class Cifar(object):
    def __init__(self):
        # 初始化操作
        self.width = 32
        self.hight = 32
        self.channels = 3

        # 字节数
        self.image_bytes = self.hight * self.width * self.channels
        self.label_bytes = 1
        self.all_bytes = self.image_bytes + self.label_bytes
    
    def read_and_decode(self, file_list):
        """
        二进制文件读取
        流程分析: 
        # 1) 构造文件名队列
        # 2) 读取与解码
        # 3) 批处理
        # 4) 
        # 5) 
        # 6) 
        
        """
        print('============================开始运行================================')
        # 1) 构造文件名队列
        file_queue = v1.train.string_input_producer(file_list)

        # 2) 读取与解码
        # 读取阶段 FixedLengthRecordReader.__init__ replaced by `tf.data`. Use `tf.data.FixedLengthRecordDataset`.
        reader = v1.FixedLengthRecordReader(self.all_bytes)
        # key: 文件名; value: 一个样本
        key, value = reader.read(file_queue)
        print('key: \n', key)
        print('value: \n', value)
        # 解码阶段
        decoded = v1.decode_raw(value, v1.uint8)
        print('decoded: \n', decoded)
        # 将目标值和特征值切开
        label = v1.slice(decoded, [0], [self.label_bytes])
        image = v1.slice(decoded, [self.label_bytes], [self.image_bytes])
        print('label: \n', label)
        print('image: \n', image)
        # 调整图片形状
        image_reshape = v1.reshape(image, shape=[self.channels, self.hight, self.width])
        print('image_reshape: \n', image_reshape)
        # 图形转置 height, width, channels
        image_transpose = v1.transpose(image_reshape,[1,2,0])
        print('image_transpose: \n', image_transpose)
        # 调整图像类型
        image_cast = v1.cast(image_transpose, v1.float32)

        # 3) 批处理
        label_batch, image_batch = v1.train.batch([label, image_cast], batch_size=100, num_threads=2, capacity=100)
        print('label_batch: \n', label_batch)
        print('image_batch: \n', image_batch)

        # 开启会话
        with v1.Session() as sess:
            # 开启线程
            # 实例化一个线程管理器
            coord = v1.train.Coordinator()
            threads = v1.train.start_queue_runners(sess=sess, coord=coord)

            key_new, value_new, decoded_new,label_new, image_new,image_reshape_new,image_transpose_new = sess.run([key, value, decoded, label, image, image_reshape,image_transpose])
            label_bnew, image_bnew = sess.run([label_batch,image_batch])
            print('key_new: \n', key_new)
            print('value_new: \n', value_new)
            print('decoded_new: \n', decoded_new)
            print('label_new: \n', label_new)
            print('image_new: \n', image_new)
            print('image_reshape_new: \n', image_reshape_new)
            print('image_transpose_new: \n', image_transpose_new)
            print('label_bnew: \n', label_bnew)
            print('image_bnew: \n', image_bnew)

            # 回收线程
            coord.request_stop()
            coord.join(threads=threads)

        print('============================结束运行================================')

        return None

if __name__ == '__main__':

    # 构造文件名
    file_names = os.listdir('./cifar-10-batches-bin')
    # 文件 = 文件名 + 路径
    file_list = [os.path.join('./cifar-10-batches-bin/', file) for file in file_names if file[-3:] == 'bin']

    # print(file_list)

    cifar = Cifar()
    cifar.read_and_decode(file_list)
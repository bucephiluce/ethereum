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
        """
        # 1) 构造文件名队列
        file_queue = v1.train.string_input_producer(file_list)

        # 2) 读取与解码
        # 读取阶段 FixedLengthRecordReader.__init__ replaced by `tf.data`. Use `tf.data.FixedLengthRecordDataset`.
        reader = v1.FixedLengthRecordReader(self.all_bytes)
        # key: 文件名; value: 一个样本
        key, value = reader.read(file_queue)
        # 解码阶段
        decoded = v1.decode_raw(value, v1.uint8)
        # 将目标值和特征值切开
        label = v1.slice(decoded, [0], [self.label_bytes])
        image = v1.slice(decoded, [self.label_bytes], [self.image_bytes])
        # 调整图片形状
        image_reshape = v1.reshape(image, shape=[self.channels, self.hight, self.width])
        # 图形转置 height, width, channels
        image_transpose = v1.transpose(image_reshape,[1,2,0])
        # 调整图像类型
        image_cast = v1.cast(image_transpose, v1.float32)

        # 3) 批处理
        label_batch, image_batch = v1.train.batch([label, image_cast], batch_size=100, num_threads=1, capacity=100)
        print('label_batch: \n', label_batch)
        print('image_batch: \n', image_batch)

        # 开启会话
        with v1.Session() as sess:
            # 开启线程
            # 实例化一个线程管理器
            coord = v1.train.Coordinator()
            threads = v1.train.start_queue_runners(sess=sess, coord=coord)

            label_bnew, image_bnew = sess.run([label_batch,image_batch])

            # 回收线程
            coord.request_stop()
            coord.join(threads=threads)

        return image_bnew, label_bnew

    def write_to_tfrecords(self, image_batch, label_batch):
        """
        将样本的特征值和目标值写入tfrecords文件
        流程分析: 
        # 1) 
        # 2) 
        # 3) 
        # 4) 
        # 5) 
        # 6) 
        
        """
        print('============================开始运行================================')

        # 将样本的特征值和目标值写入tfrecords文件
        with v1.python_io.TFRecordWriter('cifar10.tfrecords') as writer:
            # 循环构造example对象，并序列化写入文件
            for image, label in zip(image_batch, label_batch):
                # print('image: \n',image.tostring())
                # print('label: \n',label[0])
                example = v1.train.Example(features = v1.train.Features(feature = {
                    #  tostring() is deprecated. Use tobytes() instead.
                    "image": v1.train.Feature(bytes_list = v1.train.BytesList(value=[image.tobytes()])),
                    "label": v1.train.Feature(int64_list = v1.train.Int64List(value=[label[0]]))
                }))
                # 将序列化后的example写入到cifar10.tfrecords文件中
                writer.write(example.SerializeToString())

        print('============================结束运行================================')

        return None

    def read_tfrecords(self):
        """
        读取tfrecords文件
        流程分析: 
        # 1) 构造文件名队列
        # 2) 读取与解析
        # 3) 读取
        # 4) 解析example
        # 5) 解析
        # 6) 构造批处理队列
        
        """
        print('============================开始运行================================')
        # 1) 构造文件名队列
        file_queue = v1.train.string_input_producer(['cifar10.tfrecords'])

        # 2) 读取与解析
        # 2.1) 读取
        reader = v1.TFRecordReader()
        key, value = reader.read(file_queue)
        # 2.2) 解析example
        feature = v1.parse_single_example(value,features = {
			"image":v1.FixedLenFeature([],v1.string),
			"label":v1.FixedLenFeature([],v1.int64)
		})
        image = feature['image']
        label = feature['label']
        print('image: \n', image)
        print('label: \n', label)
        # 2.3) 解析 
        # 在decord_raw()时必须指定原始数据的格式，原始数据是什么格式这里解析必须是什么格式，要不然会出现形状的不对应问题！
        image_decoded = v1.decode_raw(image, v1.float32)
        print('image_decoded: \n', image_decoded)

        # 图像形状调整，动态调整，调整为tf支持的格式
        image_reshape = v1.reshape(image_decoded, shape=[self.hight, self.width, self.channels])
        print('image_reshape: \n',image_reshape)

        # 3) 构造批处理队列
        label_batch, image_batch = v1.train.batch([label, image_reshape], batch_size=100, num_threads=2, capacity=100)
        print('label_batch: \n', label_batch)
        print('image_batch: \n', image_batch)

        # 开启会话
        with v1.Session() as sess:
            # 开启线程
            # 实例化一个线程管理器
            coord = v1.train.Coordinator()
            threads = v1.train.start_queue_runners(sess=sess, coord=coord)

            label_val, image_val = sess.run([label_batch,image_batch])
            print('label_val: \n', label_val)
            print('image_val: \n', image_val)

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
    # image_bnew, label_bnew = cifar.read_and_decode(file_list)
    # cifar.write_to_tfrecords(image_bnew, label_bnew)
    cifar.read_tfrecords()
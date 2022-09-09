
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2" # 设置环境变量必须放在第一行

import tensorflow as tf
from tensorflow.python.client import device_lib
tf.compat.v1.disable_eager_execution() # 保证session.run()能够正常运行

def set_tf_devices():
    """
    指定TensorFlow的在CPU下运行
    """

    # 查看当前设备环境
    print(device_lib.list_local_devices())
    # 方法一
    # os.environ["CUDA_VISIBLE_DEVICES"] = '/device:CPU:0'

    # 方法二
    os.environ["CUDA_VISIBLE_DEVICES"]="-1"
    
    # 方法三
    # cpu=tf.config.list_physical_devices("CPU")
    # tf.config.set_visible_devices(cpu)
    print(tf.config.list_logical_devices())

def tensorflow_demo():
    """
    TensorFlow的基本结构
    """
    # python中的加法
    a = 2
    b = 3
    c = a + b
    print('python中的普通加法: \n', c)

    # Tensorflow实现加法运算
    ta = tf.constant(2)
    tb = tf.constant(3)
    tc = ta + tb
    print('Tensorflow中的加法运算结果: \n', tc)

    # init = tf.compat.v1.global_variables_initializer() # When init is run later (session.run(init)),
    # 开启会话
    with tf.compat.v1.Session() as session: 
        # session.run(init) # Initializes the variables
        tc_value = session.run(tc)
        print(tc_value)

    return None

if __name__ == '__main__':
    # 代码1: Tensorflow的基本结构
    tensorflow_demo()
    # set_tf_devices()

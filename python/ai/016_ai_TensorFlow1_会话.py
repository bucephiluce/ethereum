
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2" # 设置环境变量必须放在第一行

import tensorflow as tf
tf.compat.v1.disable_eager_execution() # 保证session.run()能够正常运行

def session_demo():
    """
    TensorFlow 会话的演示
    一句话，操作对象就是图里面一个节点，操作函数就是生成一个节点
    输入输出都是Tensor对象
    """
    print('============================开始运行================================\n')
    # Tensorflow实现加法运算
    ta = tf.constant(2, name='ta')
    tb = tf.constant(3, name='tb')
    tc = tf.add(ta,tb)
    print('ta: \n', ta)
    print('tb: \n', tb)
    print('TensorFlow中tc的加法运算结果: \n', tc)

    # 获取默认图
    default_g = tf.compat.v1.get_default_graph()
    # 方法一: 通过方法获取
    print('默认图: \n', default_g)
    # 方法二: 通过属性获取
    print("ta的图属性: \n", ta.graph)
    print("tc的图属性: \n", tc.graph)

    # 开启会话
    # 运行会话并打印设备信息
    with tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(allow_soft_placement=True, log_device_placement=True)) as session: 
        # 同时打印ta , tb, tc的值
        a, b, c = session.run([ta, tb, tc])
        print('abc: \n', a, b, c)
        # abc = session.run([ta, tb, tc])
        # print('abc: \n', abc)
        print('会话运算结果: \n',tc.eval())
        print('session的图属性: \n',session.graph)

    print('============================结束运行================================\n')
    
    return None

def placeholder_demo():
    """
    定义占位符 placeholder 需要和feed_dict 一起使用
    """
    print('============================开始运行================================\n')
    a = tf.compat.v1.placeholder(tf.float32)
    b = tf.compat.v1.placeholder(tf.float32)
    c = tf.add(a, b)

    with tf.compat.v1.Session() as sess: 
        c_value = sess.run(c , feed_dict={a:3.9,b:4.0})
        print('c_value \n', c_value)

    print('============================结束运行================================\n')
    
    return None

def tensor_demo():
    """
    张量
    """
    print('============================开始运行================================\n')
    tensor1 = tf.constant(4.0)
    tensor2 = tf.constant([1,2,3,4])  # 未指定类型，默认类型
    linear_squares = tf.constant([[4],[9],[16],[25]],dtype=tf.int32)
    print("tensor1:", tensor1)
    print("tensor2:", tensor2)
    print("linear_square_before:", linear_squares)

    # 张量类型的修改
    l_cast = tf.cast(linear_squares, dtype=tf.float32)
    print("linear_square_after:", linear_squares)
    print('l_cast: \n', l_cast)

    # 更新/改变静态形状
    # 没有完全固定下来的静态形状
    a = tf.compat.v1.placeholder(dtype=tf.float32, shape=[None, None])
    b = tf.compat.v1.placeholder(dtype=tf.float32, shape=[None, 10])
    c = tf.compat.v1.placeholder(dtype=tf.float32, shape=[2, 3])
    print('a: \n', a)
    print('b: \n', b)
    print('c: \n', c)
    # 更新形状为确定的部分
    a.set_shape([3,4])
    b.set_shape([5,10])
    print('a: \n', a)
    print('b: \n', b)


    print('============================结束运行================================\n')
    
    return None

def tensor_reshape_demo():
    """
    张量:动态形状修改
    """
    print('============================开始运行================================\n')
    
    a = tf.compat.v1.placeholder(dtype=tf.float32, shape=[None, None])
    b = tf.compat.v1.placeholder(dtype=tf.float32, shape=[None, 10])
    c = tf.compat.v1.placeholder(dtype=tf.float32, shape=[2, 3])
    print('a: \n', a)
    print('b: \n', b)
    print('c: \n', c)
    a_r = tf.reshape(a , shape=[3,4,5])
    print('a: \n', a)
    print('a_r: \n', a_r)

    # 已经固定的形状,需要保证元素数量一致
    c_r = tf.reshape(c, shape=[3,2,1])
    print('c: \n', c)
    print('c_r: \n', c_r)


    print('============================结束运行================================\n')
    
    return None

def function_demo():
    """
    
    """
    print('============================开始运行================================\n')

    print('============================结束运行================================\n')
    return None

def variable_demo():
    """
    变量演示
    """

    print('============================开始运行================================\n')
    with tf.compat.v1.variable_scope('my_scope'): 
        a = tf.Variable(initial_value=40)
        b = tf.Variable(initial_value=50)
    with tf.compat.v1.variable_scope('your_scope'): 
        c = tf.add(a, b)

    print('a: \n', a)
    print('b: \n', b)
    print('c: \n', c)

    # 初始化参数
    init = tf.compat.v1.global_variables_initializer()
    # 开启会话
    with tf.compat.v1.Session() as sess:

        # 运行初始化
        sess.run(init)
        a_val, b_val, c_val = sess.run([a, b, c])
        print('a_val: \n', a_val)
        print('b_val: \n', b_val)
        print('c_val: \n', c_val)

    print('============================结束运行================================\n')

    return None

if __name__ == '__main__':
    # 代码1: TensorFlow 会话的演示
    # session_demo()
    # 代码2: 定义占位符
    # placeholder_demo()
    # 代码3: 张量
    # tensor_demo()
    # 代码4: 张量:动态形状修改
    # tensor_reshape_demo()
    # 代码5: 变量演示
    variable_demo()


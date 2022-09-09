
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2" # 设置环境变量必须放在第一行

import tensorflow as tf
tf.compat.v1.disable_eager_execution() # 保证session.run()能够正常运行

def graph_demo():
    """
    TensorFlow 图的演示
    """
    
    # Tensorflow实现加法运算
    ta = tf.constant(2)
    tb = tf.constant(3)
    tc = ta + tb
    print('Tensorflow中的加法运算结果: \n', tc)

    # 获取默认图
    default_g = tf.compat.v1.get_default_graph()
    # 方法一: 通过方法获取
    print('默认图 default_g: \n', default_g)
    # 方法二: 通过属性获取
    print("ta的图属性: \n", ta.graph)
    print("tc的图属性: \n", tc.graph)

    # 开启会话
    with tf.compat.v1.Session() as session: 
        tc_value = session.run(tc)
        print('会话运算结果: \n',tc_value)
        print('session的图属性: \n',session.graph)

    print('============================================================\n')
    
    # 自定义图
    g = tf.Graph()
    with g.as_default(): 
        ta_new = tf.constant(20)
        tb_new = tf.constant(30)
        tc_new = ta_new + tb_new
        print('Tensorflow中tc_new的加法运算结果: \n', tc_new)
        print("ta_new的图属性: \n", ta_new.graph)
        print("tc_new的图属性: \n", tc_new.graph)

    # 开启会话
    with tf.compat.v1.Session(graph=g) as sessio_new: 
        tc_new_value = sessio_new.run(tc_new)
        print('会话运算tc_new结果: \n',tc_new_value)
        print('sessio_new的图属性: \n',sessio_new.graph)

    return None

if __name__ == '__main__':
    # 代码1: TensorFlow 图的演示
    graph_demo()

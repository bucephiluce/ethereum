
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2" # 设置环境变量必须放在第一行

import tensorflow as tf
tf.compat.v1.disable_eager_execution() # 保证session.run()能够正常运行

def graph_demo():
    """
    TensorFlow 图的演示
    一句话，操作对象就是图里面一个节点，操作函数就是生成一个节点
    输入输出都是Tensor对象
    """
    
    # Tensorflow实现加法运算
    ta = tf.constant(2, name='ta')
    tb = tf.constant(3, name='tb')
    tc = ta + tb
    tc_op = tf.add(ta,tb)
    print('ta: \n', ta)
    print('tb: \n', tb)
    print('TensorFlow中tc的加法运算结果: \n', tc)
    print('TensorFlow中tc_op的加法运算结果: \n', tc_op)

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

        # sess图序列化为summary对象
	    # 参数一：输出sumary对象的路径，参数二：需要进行序列化的图
        # 导出事件文件,可以使用tensorboard直接查看
        # 将图进行数据序列化，为events文件
        tf.compat.v1.summary.FileWriter(logdir='tmp/summary', graph=session.graph)
        # 打开终端, 启动tensorboard命令: tensorboard --logdir='./summary'

    print('============================================================\n')
    
    """
        一个图一个命名空间，互不干扰影响
        指令名称 : 每一个操作函授都有一个name属性, 都可以定义自己的指令名称
    """
    # 自定义图
    g = tf.Graph()
    with g.as_default(): 
        ta_new = tf.constant(20, name='ta_new')
        tb_new = tf.constant(30)
        tc_new = ta_new + tb_new
        print('ta_new\n',ta_new)
        print('tb_new\n',tb_new)
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

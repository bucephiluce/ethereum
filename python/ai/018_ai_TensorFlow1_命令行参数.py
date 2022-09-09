import os
# 设置环境变量必须放在第一行
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2" 

import tensorflow as tf

v1 = tf.compat.v1
# 保证session.run()能够正常运行
v1.disable_eager_execution() 

# 在命令行中需要使用 --model_path
v1.app.flags.DEFINE_string('model_path', 'tmp/model/my_linear.ckpt', '模型路径+模型名称')
FLAGS = v1.app.flags.FLAGS

def linear_regression():
    """
    自实现一个线性回归

    其中学习率和步长可以相互调整,
    学习率[0,1]: 一般设置为0.01和0.1. 如果设置太大会有梯度爆炸的风险

    流程分析: 
    1) 准备数据
    2) 构造模型
    3) 构造损失函数
    4) 优化模型-->优化损失
    5) 模型保存
    6) 命令行参数
    7) 变量的命名空间
    
    """
    print('============================开始运行================================')
    
    # 1) 准备数据
    with v1.variable_scope('prepare_data'):
        x = v1.random_normal(shape=[100,1], name='feature')
        y_true = v1.matmul(x, [[0.8]]) + 0.7

    with v1.variable_scope('create_model'):
        # 2) 构造模型 
        # y = w1x1+w2x2+...+wnxn+bias
        # Variable 默认:trainable=True
        weights = v1.Variable(initial_value=v1.random_normal(shape=[1,1]), name='Weights')
        bias = v1.Variable(initial_value=v1.random_normal(shape=[1,1]), trainable=True, name='Bias')
        y_predict = v1.matmul(x, weights) + bias

    with v1.variable_scope('loss_function'):
        # 3) 构造损失函数 均方误差
        error = tf.reduce_mean(tf.square(y_predict - y_true))

    with v1.variable_scope('optimizer'):
        # 4) 优化模型-->优化损失
        optimizer = v1.train.GradientDescentOptimizer(learning_rate=0.05).minimize(error)

    # 2_ 收集变量 用于 tensorboard 的可视化
    # 2_1_ 收集标量
    v1.summary.scalar('error', error)
    # 2_2_ 收集高纬度变量
    v1.summary.histogram('weights', weights)
    v1.summary.histogram('bias', bias)
    # 3_合并变量
    merged = v1.summary.merge_all()

    # 实例化模型保存
    saver = v1.train.Saver()

    # 显示地初始化变量
    init = v1.global_variables_initializer()

    # 开启会话
    with v1.Session() as sess:
        # 初始化变量
        sess.run(init)

        print('训练前的模型参数: 权重: {0}, 偏置: {1}, 损失为: {2}'.format(weights.eval(),bias.eval(),error.eval()))

        # 加载模型 当存在checkpoint 就加载模型
        if os.path.exists('tmp/model/checkpoint'):
            saver.restore(sess, FLAGS.model_path)

        # 1_ 创建事件文件
        file_writer = v1.summary.FileWriter(logdir='tmp/linear', graph=sess.graph)

        # 开始训练 并且设置步长
        for i in range(100) :
            step = i+1
            sess.run(optimizer)
            print('第{3}次训练后的模型参数: 权重: {0}, 偏置: {1}, 损失为: {2}'.format(weights.eval(),bias.eval(),error.eval(),step))
            # 4_运行合并变量操作
            summary = sess.run(merged)
            # 5_每次迭代之后重新将变量写入事件文件
            file_writer.add_summary(summary,step)

            # 保存模型 checkpoint=ckpt
            if step % 10 == 0 :
                saver.save(sess, FLAGS.model_path)

    print('============================结束运行================================')

def main(argv):
    print('这是main函数')
    print(argv)
    print(FLAGS.model_path)
    linear_regression()

if __name__ == '__main__':
    v1.app.run()
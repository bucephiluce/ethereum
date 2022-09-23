"""
线性模型实战
y = 1.477 * x + 0.089 + eps
"""
import numpy as np

# 保存样本集的列表
data = []
for i in range(100):
    # 随机采样输入 x
    x = np.random.uniform(-10,10)
    # 采样高斯噪声
    eps = np.random.normal(loc=0., scale=0.01)
    # 得到模型输出
    y = 1.477 * x + 0.089 + eps
    data.append([x, y])

# 转换为 2D Numpy 数组
data = np.array(data)

def mse(b, w, points):
    """
    构造均方误差 :
    loss = (w*x+b - y)**2
    """
    total_error = 0
    for i in range(len(points)):
        x = points[i,0]
        y = points[i,1]
        total_error += (w*x+b - y)**2

    return total_error/float(len(points))

def step_gradient(b, w, points , lr):
    """
    计算梯度:
    w_new = w - 2*(w*x+b-y)*x
    b_new = b - 2*(w*x+b-y)
    """
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points[i,0]
        y = points[i,1]
        b_gradient += 2*(w*x+b-y)/N
        w_gradient += 2*(w*x+b-y)*x/N

    b_new = b - b_gradient*lr
    w_new = w - w_gradient*lr
    return b_new, w_new

def gradient_descent_runner(points, starting_b, starting_w, learning_rate, num_iterations):
    b = starting_b
    w = starting_w
    # update for several times
    for i in range(num_iterations):
        step = i+1
        b, w = step_gradient(b, w, points, learning_rate)
        loss = mse(b, w, points) # 计算当前的均方差，用于监控训练进度
        if step%50 == 0: # 打印误差和实时的 w,b 值
            print(f"iteration:{step}, loss:{loss}, w:{w}, b:{b}")
    return [b, w]


def run():
	
    points = data
    learning_rate = 0.01 # 0.001, 0.0001都不一样
    initial_b = 0 # initial y-intercept guess
    initial_w = 0 # initial slope guess
    num_iterations = 1000
    print("Starting gradient descent at b = {0}, w = {1}, error = {2}"
          .format(initial_b, initial_w,
                  mse(initial_b, initial_w, points))
          )
    print("Running...")
    [b, w] = gradient_descent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, w = {2}, error = {3}".
          format(num_iterations, b, w,
                 mse(b, w, points))
          )

if __name__ == '__main__':
    run()
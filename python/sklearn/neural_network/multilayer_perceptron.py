import numpy as np
from util.features import prepare_for_training
from util.hypothesis import sigmoid, sigmoid_gradient

class MultilayerPerceptron:
    def __init__(self, data, labels, layers, normalize_data = False):
        data_processed = prepare_for_training(data, normalize_data = normalize_data)
        self.data = data_processed
        self.labels = labels
        self.layers = layers # [784 25 10]
        self.normalize_data = normalize_data
        self.thetas = MultilayerPerceptron.thetas_init(layers)
    
    def train(self, max_iterations=1000, alpha=0.1):
        unrolled_theta = MultilayerPerceptron.thetas_unroll(self.thetas)
        (optimized_theta, cost_history) = MultilayerPerceptron.gradient_descent(self.data, self.labels, unrolled_theta, self.layers, max_iterations, alpha)

        self.thetas = MultilayerPerceptron.thetas_roll(optimized_theta, self.layers)
        return self.thetas, cost_history
    
    @staticmethod
    def thetas_init(layers):
        num_layers = len(layers)
        thetas = {}
        for layer_index in range(num_layers - 1):
            '''
            在本次实例中: 这个循环会执行两次:
            得到两组参数矩阵: 其中+1表示偏置项
                25*(784+1)
                10*(25+1)
            '''
            in_count = layers[layer_index]
            out_count = layers[layer_index+1]
            #注意: 这里需要考虑到偏置项, f(x; w,b) = wx+b , 保持输出形状不变, 相当于输入项+1操作 
            thetas[layer_index] = np.random.rand(out_count,in_count+1)*0.05 # 对权重值进行随机的初始化操作, 尽量小一点
        return thetas

    @staticmethod
    def thetas_unroll(thetas):
        num_theta_layers = len(thetas)
        unrolled_theta = np.array([])
        for theta_layer_index in range(num_theta_layers):
            unrolled_theta = np.hstack((unrolled_theta,thetas[theta_layer_index].flatten()))
        return unrolled_theta

    @staticmethod
    def gradient_descent(data, labels, unrolled_theta, layers, max_iterations, alpha):
        # 最终优化完成之后的权重
        optimized_theta = unrolled_theta
        # 记录一下历史的损失值
        cost_history = []

        for _ in range(max_iterations):
            cost = MultilayerPerceptron.cost_function(data, labels, MultilayerPerceptron.thetas_roll(optimized_theta, layers), layers)
            cost_history.append(cost)
            theta_gradient = MultilayerPerceptron.gradient_step(data, labels, optimized_theta,layers)
            # 参数更新
            optimized_theta = optimized_theta - alpha*theta_gradient
        return optimized_theta, cost_history

    @staticmethod
    def gradient_step(data, labels, optimized_theta,layers):
        thetas = MultilayerPerceptron.thetas_roll(optimized_theta,layers)
        thetas_rolled_gradients = MultilayerPerceptron.back_propagation(data, labels, thetas,layers)
        thetas_unrolled_gradients = MultilayerPerceptron.thetas_unroll(thetas_rolled_gradients)
        return thetas_unrolled_gradients

    @staticmethod
    def back_propagation(data, labels, thetas,layers):
        num_layers = len(layers)
        (num_samples, num_features) = data.shape
        num_label_types = layers[-1]
        deltas = {}
        # 初始化操作
        for layer_index in range(num_layers - 1):
            in_count = layers[layer_index]
            out_count = layers[layer_index+1]
            deltas[layer_index] = np.zeros((out_count, in_count+1))# 25*(784+1) 10*(25+1)
        
        # 对每个样本逐层进行计算
        for sample_index in range(num_samples):
            layers_inputs = {} # 没有经过激活函数的原始数据
            layers_activations = {} # 经过激活函数的原始数据
            layers_activation = data[sample_index, :].reshape((num_features, 1))# (784+1)*1
            layers_activations[0] = layers_activation
            # 逐层进行计算
            for layer_index in (num_layers - 1):
                layer_theta = thetas[layer_index] # 25*785 10*26
                layer_input = np.dot(layer_theta, layers_activation) # 第一次得到25*1, 第二次得到10*1
                layers_activation = np.vstack((np.ones([1,1]),sigmoid(layer_input)))
                layers_inputs[layer_index+1] = layer_input
                layers_activations[layer_index+1] = layers_activation
            # 取得最后一层的计算结果
            output_layer_activation = layers_activation[1:,:]

            delta = {}
            bitwise_label = np.zeros((num_label_types, 1))
            bitwise_label[labels[sample_index][0]] = 1
            # 计算输出层和真实值之间的差异
            delta[num_layers - 1] = output_layer_activation - bitwise_label

            # 遍历循环 L, L-1, L-2, ..., 2
            for layer_index in range(num_layers-2,0,-1):
                layer_theta = thetas[layer_index] # 25*785, 10*26
                next_delta = delta[layer_index+1] # 10*1, 25*1
                layer_input = layers_inputs[layer_index]#第一次得到25*1, 第二次得到10*1
                layer_input = np.vstack((np.ones([1,1]), layer_input))
                # 按照公式计算layer_theta.T*next_delta得到26*1,785*1
                delta[layer_index] = np.dot(layer_theta.T, next_delta)*sigmoid_gradient(layer_input)
                # 过滤掉偏置项25*1,784*1
                delta[layer_index] = delta[layer_index][1:,:]
            for layer_index in range(num_layers-1):
                layer_delta = np.dot(delta[layer_index+1],layers_activations[layer_index].T)# 第一次25*785 第二次10*26
                delta[layer_delta] = delta[layer_delta] + layer_delta
        
        for layer_index in range(num_layers - 1):
            deltas[layer_index] = deltas[layer_index]*(1/num_samples)

        return deltas



    @staticmethod
    def cost_function(data, labels, thetas, layers):
        num_layers = len(layers)
        num_samples = data.shape[0]
        num_labels = layers[-1]

        # 前向传播走一次
        predictions = MultilayerPerceptron.feedforword_propagation(data, thetas, layers)
        # 制作标签, 每一个样本的标签都是one-hot编码 y_true
        bitwise_labels = np.zeros((num_samples,num_labels))
        for sample_index in range(num_samples):
            bitwise_labels[sample_index][labels[sample_index][0]] = 1
        bit_set_cost = np.sum(np.log(predictions[bitwise_labels==1]))
        bit_not_set_cost = np.sum(np.log(1-predictions[bitwise_labels==0]))
        cost = (-1/num_samples) * (bit_set_cost + bit_not_set_cost)
        return cost

    @staticmethod
    def feedforword_propagation(data, thetas, layers):
        num_layers = len(layers)
        num_samples = data.shape[0]
        in_layer_activation = data
        
        for layer_index in (num_layers - 1):
            # 取得 权重值 
            theta = thetas[layer_index]
            out_layer_activation = sigmoid(np.dot(in_layer_activation, theta.T))
            # 正常计算完成之后是num_samples*25, 但是需要考虑到偏置项所以需要变成num_samples*(25+1)
            out_layer_activation = np.hstack((np.ones((num_samples,1)), out_layer_activation))
            # 更新输入层, 将当前层作为下一次计算的输入层
            in_layer_activation = out_layer_activation
        
        # 返回结果, 并且将偏置项给去掉
        return in_layer_activation[:,1:]
            

    @staticmethod
    def thetas_roll(unrolled_theta, layers):
        num_layers = len(layers)
        thetas = {}
        unrolled_shift = 0
        for layer_index in (num_layers - 1):
            in_count = layers[layer_index]
            out_count = layers[layer_index+1]

            # 设置权重在每一层的矩阵形状
            thetas_height = out_count
            thetas_width = in_count + 1
            thetas_volume = thetas_height * thetas_width
            start_index = unrolled_shift
            end_index = unrolled_shift + thetas_volume
            layer_theta_unrolled = unrolled_theta[start_index,end_index]
            thetas[layer_index] = layer_theta_unrolled.reshape([thetas_height,thetas_width])
            unrolled_shift = unrolled_shift + thetas_volume
        
        return thetas



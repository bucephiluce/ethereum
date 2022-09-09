from sklearn.linear_model import LinearRegression , SGDRegressor , Ridge
# load_boston 已经弃用
# from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import joblib
# sklearn.externals.joblib函数是用在0.21及以前的版本中，在最新的版本中，该函数应被弃用改为直接导入joblib
# from sklearn.externals import joblib
import pandas as pd
import numpy as np

def linear1(): 
    """
    正规方程的优化方法对波士顿房价进行预测
    1. 获取数据
    2. 划分数据集
    3. 特征工程: 特征值标准化抽取
    4. 预估器
    5. 得出模型
    6. 模型评估
    """
    # 1. 获取数据
    # boston = load_boston() # 已经过时
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]

    # 2. 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(data, target, random_state=23)

    # 3. 特征工程: 特征值标准化抽取
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4. 预估器
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)

    # 5. 得出模型
    print('正规方程 - 权重参数为: \n', estimator.coef_)
    print('正规方程 - 偏置为: \n', estimator.intercept_)

    # 6. 模型评估
    y_predict = estimator.predict(x_test)
    print('预测房价:\n', y_predict)
    error = mean_squared_error(y_test, y_predict)
    print('正规方程 - 均方误差模型评估: \n', error)

def linear2(): 
    """
    梯度下降的优化方法对波士顿房价进行预测
    1. 获取数据
    2. 划分数据集
    3. 特征工程: 特征值标准化抽取
    4. 预估器
    5. 得出模型
    6. 模型评估
    """
    # 1. 获取数据
    # boston = load_boston() # 已经过时
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]

    # 2. 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(data, target, random_state=23)

    # 3. 特征工程: 特征值标准化抽取
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4. 预估器
    estimator = SGDRegressor(penalty='l1')
    estimator.fit(x_train, y_train)

    # 5. 得出模型
    print('梯度下降 - 权重参数为: \n', estimator.coef_)
    print('梯度下降 - 偏置为: \n', estimator.intercept_)

    # 6. 模型评估
    y_predict = estimator.predict(x_test)
    print('预测房价:\n', y_predict)
    error = mean_squared_error(y_test, y_predict)
    print('梯度下降 - 均方误差模型评估: \n', error)

def linear3(): 
    """
    岭回归的优化方法对波士顿房价进行预测
    1. 获取数据
    2. 划分数据集
    3. 特征工程: 特征值标准化抽取
    4. 预估器
    5. 得出模型
    6. 模型评估
    """
    # 1. 获取数据
    # boston = load_boston() # 已经过时
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]

    # 2. 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(data, target, random_state=23)

    # 3. 特征工程: 特征值标准化抽取
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4. 预估器
    # estimator = Ridge()
    # estimator.fit(x_train, y_train)

    # 保存模型
    # joblib.dump(estimator, 'python/ai/my_ridge.pkl')
    # 加载模型
    estimator = joblib.load('python/ai/my_ridge.pkl')

    # 5. 得出模型
    print('岭回归 - 权重参数为: \n', estimator.coef_)
    print('岭回归 - 偏置为: \n', estimator.intercept_)

    # 6. 模型评估
    y_predict = estimator.predict(x_test)
    print('预测房价:\n', y_predict)
    error = mean_squared_error(y_test, y_predict)
    print('岭回归 - 均方误差模型评估: \n', error)

if __name__ == '__main__':
    # 代码1: 正规方程的优化方法对波士顿房价进行预测
    # linear1()
    # 代码2: 梯度下降的优化方法对波士顿房价进行预测
    # linear2()
    # 代码3: 岭回归的优化方法对波士顿房价进行预测
    linear3()

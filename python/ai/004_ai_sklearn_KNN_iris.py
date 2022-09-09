from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

def knn_iris():
    """
    用K-近邻算法(KNN)对鸢尾花进行分类
    1) 获取数据
    2) 对数据集划分
    3) 特征工程: 标准化
    4) KNN算法预估器
    5) 模型评估
    """

    # 1) 获取数据
    iris = load_iris()

    # 2) 对数据集划分
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=23)

    # 3) 特征工程: 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    # 使用训练集计算(fit)出来的均值和标准值来对测试集进行转化, 保持一致
    x_test = transfer.transform(x_test)

    # 4) KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)

    # 5) 模型评估
    # 方法一: 直接对比真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict: \n', y_predict)
    print('直接对比真实值和预测值: \n', y_test == y_predict)

    # 方法二: 计算准确率
    score = estimator.score(x_test,y_test)
    print('准确率: \n', score)

    return None

def knn_iris_gscv():
    """
    用K-近邻算法(KNN)对鸢尾花进行分类, 添加网格搜索和交叉验证
    1) 获取数据
    2) 对数据集划分
    3) 特征工程: 标准化
    4) KNN算法预估器
    5) 模型评估
    """

    # 1) 获取数据
    iris = load_iris()

    # 2) 对数据集划分
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=23)

    # 3) 特征工程: 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    # 使用训练集计算(fit)出来的均值和标准值来对测试集进行转化, 保持一致
    x_test = transfer.transform(x_test)

    # 4) KNN算法预估器
    estimator = KNeighborsClassifier()
    # 网格搜索和交叉验证 , 模型优化调整
    param_grid = {
        'n_neighbors':[1,3,5,7,9,11]
    }
    estimator = GridSearchCV(estimator, param_grid=param_grid, cv=10)
    estimator.fit(x_train, y_train)

    # 5) 模型评估
    # 方法一: 直接对比真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict: \n', y_predict)
    print('直接对比真实值和预测值: \n', y_test == y_predict)

    # 方法二: 计算准确率
    score = estimator.score(x_test,y_test)
    print('准确率: \n', score)

    print('最佳参数:\n', estimator.best_params_)
    print('最佳结果:\n', estimator.best_score_)
    print('最佳估计器:\n', estimator.best_estimator_)
    print('交叉验证结果:\n', estimator.cv_results_)

    return None

if __name__ == '__main__':
    knn_iris()

    # knn_iris_gscv()

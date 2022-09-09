from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz

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

def decisiontree_iris():
    """
    用决策树对鸢尾花进行分类
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


    # 3) 决策树算法预估器 - 信息增益
    estimator = DecisionTreeClassifier(criterion='entropy')
    estimator.fit(x_train, y_train)

    # 4) 模型评估
    # 方法一: 直接对比真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict: \n', y_predict)
    print('直接对比真实值和预测值: \n', y_test == y_predict)

    # 方法二: 计算准确率
    score = estimator.score(x_test,y_test)
    print('准确率: \n', score)

    # 决策树的可视化
    export_graphviz(estimator, out_file='python/ai/iris-tree.dot', feature_names=iris.feature_names)

    return None

if __name__ == '__main__':
    # 对比一下两个算法的准确率
    # knn_iris()
    decisiontree_iris()

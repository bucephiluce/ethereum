from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def nb_news():
    """
    用朴素贝叶斯算法对新闻进行分类
    """
    # 1. 获取数据
    news = fetch_20newsgroups(data_home='./data' , subset='all')

    # 2. 划分数据
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, random_state=23)

    # 3.特征工程: 文本特征值抽取-tfidf
    transfer = TfidfVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4.朴素贝叶斯算法预估器
    estimator = MultinomialNB()
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

if __name__ == '__main__':
    nb_news()
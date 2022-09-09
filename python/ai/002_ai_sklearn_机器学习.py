from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from scipy.stats import pearsonr
import jieba
import pandas as pd

def datasets_demo():
    """
    sklearn数据集使用
    """

    # 获取数据集
    iris = load_iris()
    print('鸢尾花数据集: \n', iris)
    print('鸢尾花数据集描述: \n', iris['DESCR'])
    print('查看特征值的名字: \n', iris.feature_names)
    print('查看特征值: \n', iris.data, iris.data.shape)

    # 数据集划分 
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=23)
    print('训练集特征值: \n', x_train, x_train.shape)
    print('测试集特征值: \n', x_test, x_test.shape)
    print('训练集目标值: \n', y_train, y_train.shape)
    print('测试集目标值: \n', y_test, y_test.shape)

    return None

def dict_demo():
    """
    字典特征值抽取
    """
    data = [{'city':'北京','temperature':100},
            {'city':'上海','temperature':60},
            {'city':'杭州','temperature':30}]
    # 1. 实例化一个转换器类
    transfer = DictVectorizer(sparse=True) # sparse 默认为True, 返回一个稀疏矩阵

    # 2. 调用转化特征值
    data_new = transfer.fit_transform(data)
    print('data_new 稀疏矩阵展示: \n', data_new , type(data_new))
    print('data_new 二维数组展示: \n', data_new.toarray() , type(data_new))
    print('特征值名称: \n', transfer.get_feature_names_out())

    return None

def text_count_demo():
    """
    文本特征值抽取: CountVectorizer
    """
    data = ['life is short, i like like python', 'life is too too long, i too dislike python']
    # 1. 实例化一个转换器类
    transfer = CountVectorizer(stop_words=['is','too'])
    # 2. 调用fit_transform
    data_new = transfer.fit_transform(data)
    print('data_new 稀疏矩阵展示: \n', data_new , type(data_new))
    print('data_new 二维数组展示: \n', data_new.toarray() , type(data_new))
    print('特征值名称: \n', transfer.get_feature_names_out())

    return None

def text_count_chinese_demo():
    """
    中文文本特征值抽取: CountVectorizer
    中文文本处理需要先进行分词: jieba
    """
    # 将中文文本进行分词
    data = ['我是帅哥,我是帅哥,我是帅哥,重要的事情说三遍', '我爱北京天安门,天安门前红旗飘']
    data_cut = []
    for text in data:
        data_cut.append(cut_words(text=text))
    # 1. 实例化一个转换器类
    transfer = CountVectorizer()
    # 2. 调用fit_transform
    data_new = transfer.fit_transform(data_cut)
    # print('data_new 稀疏矩阵展示: \n', data_new , type(data_new))
    # print('data_new 二维数组展示: \n', data_new.toarray() , type(data_new))
    print('data_new 二维数组展示: \n', data_new.toarray())
    print('特征值名称: \n', transfer.get_feature_names_out())

    return None

def text_tfidf_chinese_demo():
    """
    用TF-IDF的方法进行文本特征值抽取: TfidfVectorizer
    """
    # 将中文文本进行分词
    data = ['我是帅哥,我是帅哥,我是帅哥,重要的事情说三遍', '我爱北京天安门,天安门前红旗飘']
    data_cut = []
    for text in data:
        data_cut.append(cut_words(text=text))
    # 1. 实例化一个转换器类
    transfer = TfidfVectorizer()
    # 2. 调用fit_transform
    data_new = transfer.fit_transform(data_cut)
    print('data_new 二维数组展示: \n', data_new.toarray())
    print('特征值名称: \n', transfer.get_feature_names_out())

    return None

def cut_words(text):
    """
    中文分词
    """
    return " ".join(jieba.cut(text))

def minmax_demo():
    """
    归一化: MinMaxScaler
    """
    # 1. 提取数据
    data = pd.read_csv('dating.txt')
    data = data.iloc[:,:3]
    # 2. 实例化一个转换器类
    transfer = MinMaxScaler(feature_range=[0,1])
    # 3. 调用fit_transform
    data_new = transfer.fit_transform(data)
    print('data_new 二维数组展示: \n', data_new)
    print('特征值名称: \n', transfer.get_feature_names_out())
    return None

def stand_demo():
    """
    标准化: StandardScaler
    """
    # 1. 提取数据
    data = pd.read_csv('dating.txt')
    data = data.iloc[:,:3]
    # 2. 实例化一个转换器类
    transfer = StandardScaler()
    # 3. 调用fit_transform
    data_new = transfer.fit_transform(data)
    print('data_new 二维数组展示: \n', data_new)
    print('特征值名称: \n', transfer.get_feature_names_out())
    return None

def variance_demo():
    """
    低方差过滤: VarianceThreshold
    """
    data = pd.read_csv('factor.csv')
    data = data.iloc[:,1:-2]
    transfer = VarianceThreshold()
    # transfer = VarianceThreshold(threshold=5)
    # 3. 调用fit_transform
    data_new = transfer.fit_transform(data)
    print('data_new 二维数组展示: \n', data_new , data_new.shape)
    print('特征值名称: \n', transfer.get_feature_names_out())

    return None

def pearsonr_demo():
    """
    计算相关系数
    """
    data = pd.read_csv('factor.csv')
    data = data.iloc[:,1:-2]
    factor = data.columns
    for i in range(len(factor)):
        for j in range(i, len(factor) - 1):
            print(
                "指标%s与指标%s之间的相关性大小为%f" % (factor[i], factor[j + 1], pearsonr(data[factor[i]], data[factor[j + 1]])[0])
                )
    return None

def pca_demo():
    """
    主成分分析PCA
    """
    data = [[2,8,4,5],[6,3,0,8],[5,4,9,1]]

    # transfer = PCA(n_components=2) # 整数: 表示减少到多少特征
    transfer = PCA(n_components=0.95) # 小数: 表示保留多少信息

    data_new = transfer.fit_transform(data)

    print('data_new 二维数组展示: \n', data_new , data_new.shape)

    return None

if __name__ == '__main__':
# 数据集

    # 代码1: sklearn数据集使用: load_*
    # datasets_demo()

# 特征提取

    # 代码2: 字典特征值抽取: DictVectorizer
    # dict_demo()
    # 代码3: 文本特征抽取: CountVectorizer
    # text_count_demo()
    # 代码4: 中文文本特征值抽取: CountVectorizer
    # text_count_chinese_demo()
    # 代码5: 中文分词
    # cut_words(text)
    # 代码6: 用TF-IDF的方法进行文本特征值抽取: TfidfVectorizer
    # text_tfidf_chinese_demo()
    
# 特征预处理
    
    # 代码7: 归一化: MinMaxScaler
    # minmax_demo()
    # 代码8: 标准化: StandardScaler
    # stand_demo()

# 特征降维

    # 代码9: 低方差过滤: VarianceThreshold
    # variance_demo()
    # 代码10: 计算相关系数
    # pearsonr_demo()
    # 代码11: 主成分分析PCA
    pca_demo()

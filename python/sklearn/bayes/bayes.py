import numpy as np
import re
import random

def textParse(input_string):
    listofTokens = re.split(r'\W+', input_string)
    return [tok.lower() for tok in listofTokens if len(listofTokens) > 2]

def createVocablist(doclist):
    '''
        创建语料库
    '''
    vocabSet = set([])
    for document in doclist:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWord2Vec(vocablist, document):
    '''
        进行文章向量化, 表示这个单词是否出现在语料库中
        出现:1
        没出现:0
    '''
    returnVec = [0]*len(vocablist)
    for word in document:
        if word in vocablist:
            returnVec[vocablist.index(word)] = 1
    return returnVec

def trainNB(trainMat, trainClass):
    numTrainDocs = len(trainMat)
    numWords = len(trainMat[0])
    # 计算是垃圾邮件的概率
    p1 = sum(trainClass)/float(numTrainDocs)
    p0Num = np.ones((numWords)) #做了一个平滑处理
    p1Num = np.ones((numWords)) #拉普拉斯平滑
    p0Denom = 2
    p1Denom = 2 # 通常情况下都是设置成类别个数

    for i in range(numTrainDocs):
        if trainClass[i] == 1 :
            p1Num += trainMat[i]
            p1Denom += sum(trainMat[i])
        else:
            p0Num += trainMat[i]
            p0Denom += sum(trainMat[i])

    # p1Vec, p0Vec这个值计算完成之后会非常小, 需要进行对数化操作
    p1Vec = np.log(p1Num/p1Denom)
    p0Vec = np.log(p0Num/p0Denom)

    return p0Vec, p1Vec, p1

def classifyNB(wordVec, p0Vec, p1Vec, p1_class):
    # 核心计算公式, 因为变成了log对数,所以是sum操作
    p1 = np.log(p1_class) + sum(wordVec*p1Vec)
    p0 = np.log(1.0 - p1_class) + sum(wordVec*p0Vec)
    if p0>p1:
        return 0
    else:
        return 1


def spam():
    '''
        垃圾邮件识别
    '''
    doclist = []
    classlist = []
    for i in range(1,26):
        wordlist = textParse(open('email/spam/%d.txt'%i,'r').read())
        doclist.append(wordlist)
        classlist.append(1) # 1表示垃圾邮件

        wordlist = textParse(open('email/ham/%d.txt'%i,'r').read())
        doclist.append(wordlist)
        classlist.append(0) # 0表示正常邮件
    # 创建语料库
    vocablist = createVocablist(doclist)
    trainSet = list(range(50))
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0,len(trainSet)))
        testSet.append(trainSet[randIndex])
        del (trainSet[randIndex])

    # 提取训练数据
    trainMat = []
    trainClass = []
    for docIndex in trainSet:
        trainMat.append(setOfWord2Vec(vocablist, doclist[docIndex]))
        trainClass.append(classlist[docIndex])
    # 进行训练
    (p0Vec, p1Vec, p1) = trainNB(np.array(trainMat), np.array(trainClass))

    # 开始测试
    errorCount = 0
    for docIndex in testSet:
        wordVec = setOfWord2Vec(vocablist, doclist[docIndex])
        if classifyNB(np.array(wordVec), p0Vec, p1Vec, p1) != classlist[docIndex] :
            errorCount += 1
    print('测试{}个数据, 错误了{}个, 错误率:{}'.format(len(testSet),errorCount,errorCount/float(len(testSet))))
import feedparser
from numpy import *
import matplotlib.pyplot as plt
def load_data():
    data_train = []
    label_train = []
    data_test = []
    label_test = []

    for lines in open("horseColicTraining.txt").readlines():
        lines = lines.strip().split()
        temp1 = []

        for num in lines:
            temp1.append(float(num))
        data_train.append(temp1[0:-1])
        label_train.append(temp1[-1])
        # data_train = data_train.append(lines)
    for lines in open("horseColicTest.txt").readlines():
        lines = lines.strip().split()
        temp2 = []
        for num in lines:
            temp2.append(float(num))
        data_test.append(temp2[0:-1])
        label_test.append(temp2[-1])
        # data_test = data_test.append(lines)
    return data_train,label_train,data_test,label_test
def sigmoid(x):
    return 1/(1+exp(-x))
def train(data_train,label_train,aa,iteration_num):
    data_train = mat(data_train)
    data_test = mat(label_train)
    m,n = data_train.shape
    w = ones((1,n))
    log = ones((iteration_num,n))

    for j in range(iteration_num):
        for i in range(m):
            wt = w.transpose()
            randindex = random.uniform(0,m)
            randindex = int(randindex)
            a = 4/(1.0+j+i)+aa
            error = label_train[randindex]-sigmoid(data_train[randindex]*wt)
            w = w + a*error*data_train[randindex]
            log[j,:] = w
    return w,log
def prediction(x):
    if x>0.5:
        return 1
    else:
        return 0
def test(data_test,label_test,w):
    m = len(data_test)
    data_test = mat(data_test)
    label_test = mat(label_test)
    res = zeros(m)
    for i in range(m):
        pre = prediction(sigmoid(data_test[i]*w.transpose()))
        print("The label is %d, the prediction is %d" % (label_test[0,i],pre))
        if pre == label_test[0,i]:
            res[i] = 1
    acc = sum(res)/len(res)*100
    return acc
if __name__ == "__main__":
    iterationnum = input("Please input the iterationnum:")
    iterationnum = int(iterationnum)
    data_train,label_train,data_test,label_test = load_data()
    w,logd = train(data_train,label_train,0.00001,iterationnum)
    acc = test(data_test,label_test,w)
    print(acc)
    x = linspace(0,iterationnum,iterationnum)
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax1.plot(x,logd[:,0])
    ax2 = fig.add_subplot(222)
    ax2.plot(x,logd[:,1])
    ax3 = fig.add_subplot(223)
    ax3.plot(x,logd[:,2])
    ax4 = fig.add_subplot(224)
    ax4.plot(x,logd[:,3])
    plt.show()


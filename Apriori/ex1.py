from numpy import *

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
def createcl(dataset):
    c1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    c1 = map(frozenset,c1)
    d = list()
    for item in c1:
        d.append(item)
    return d
def scand(d,ck,minsupport):
    sscnt = {}
    for tid in d:
        for can in ck:
            if can.issubset(tid):
                if can not in sscnt:
                    sscnt[can] = 1
                else:
                    sscnt[can]+=1

    numitems = float(len(d))
    retlist = []
    supportdata = {}
    for key in sscnt:
        support = sscnt[key]/numitems
        if support >= minsupport:
            retlist.append(key)
        supportdata[key] = support
    retlist.sort()


    return retlist,supportdata
def apriorigen(lk,k):
    retlist = []
    lenlk = len(lk)
    for i in range(lenlk):
        for j in range(i+1,lenlk):
            l1 = list(lk[i])[:k-2]
            l2 = list(lk[j])[:k-2]
            l1.sort()
            l2.sort()
            if l1==l2:
                retlist.append(lk[i]|lk[j])
    return retlist
def exercise(lk):
    retlist = []
    lk = list(lk)
    lenlk = len(lk)
    for i in range(lenlk):
        for j in range(i+1,lenlk):
            l1 = set(lk[i])
            l2 = set(lk[j])
            retlist.append(list(l1|l2))
    return retlist

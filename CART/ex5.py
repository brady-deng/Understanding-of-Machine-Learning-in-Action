import regTrees
from numpy import *

# mydat = regTrees.loadDataSet('ex00.txt')
# mydat = mat(mydat)
# print(regTrees.createTree(mydat))
#
# testmat = mat(eye(4))
# mat0,mat1 = regTrees.binSplitDataSet(testmat,1,0.5)
# print(mat0,mat1)

mydat = regTrees.loadDataSet('ex2.txt')
mydat = mat(mydat)
mytree = regTrees.createTree(mydat,ops=(0,1))
mytest = regTrees.loadDataSet('ex2test.txt')
mytest = mat(mytest)
print(regTrees.prune(mytree,mytest))
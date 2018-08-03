import svdRec
from numpy import *
#基于奇异值分解的餐馆菜肴推荐系统
#原始数据矩阵的行为不同的顾客，列为对不同菜肴的的打分
#满分为5分，0分表示没有打分
mymat = mat(svdRec.loadExData2())
mymat[0,1]=mymat[0,0]=mymat[1,0]=mymat[2,0]=4
mymat[3,3]=2
print(svdRec.recommend(mymat,1,estMethod=svdRec.svdEst))

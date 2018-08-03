import svdRec
import numpy as np
import numpy.linalg as la
np.set_printoptions(threshold=1e6) #全部输出
#基于奇异值分解的图像压缩，通过将原始图像矩阵进行奇异值分解
#然后取分解后的奇异矩阵的主要奇异值对原始图像进行压缩

data = []
numsv = 3
for line in open("0_5.txt").readlines():
    newrow = []
    for i in range(32):
        newrow.append(int(line[i]))
    data.append(newrow)
# svdRec.imgCompress(2)
# print(data)
# print(len(data))
# print(len(data[0]))
d = np.mat(data)
# print(d.shape)
print(d)
U,Sigma,VT = la.svd(d)
# print(Sigma)
sigrecon = np.mat(np.zeros((numsv,numsv)))
for k in range(numsv):
    sigrecon[k,k] = Sigma[k]
res = U[:,:numsv]*sigrecon*VT[:numsv,:]
m,n = res.shape
temp = np.zeros((m,n),dtype=np.int8)
for i in range(m):
    for j in range(n):
        if res[i,j]>0.8:temp[i,j] = int(1)
        else: temp[i,j] = int(0)

print(temp)
print(d.shape)
print(temp.shape)
file = open('1.txt','w')
for item in temp:
    file.write(str(item))
    file.write('\n')
file.close()



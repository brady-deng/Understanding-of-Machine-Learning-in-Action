import ex1
import apriori

data = ex1.loadDataSet()
c1 = ex1.createcl(data)
print(c1)
print(data)
# d = map(set,data)
l1,supportdata = ex1.scand(data,c1,0.5)
print(l1)
print(supportdata)
k = 2
l = [l1]


# ck = ex1.apriorigen(l,k)
# print(ck)
while (len(l[k-2])>0):
    ck = ex1.apriorigen(l[k-2],k)
    lk,supk = ex1.scand(data,ck,0.5)
    supportdata.update(supk)
    l.append(lk)
    k += 1

print(l,k)
rules = apriori.generateRules(l,supportdata,minConf=0.7)
print(rules)
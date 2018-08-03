import ex3

simpdat = ex3.loadSimpDat()
print(simpdat)
initset = ex3.createInitSet(simpdat)
print(initset)
myfptree,myheadertab = ex3.createtree(initset,3)
myfptree.disp()
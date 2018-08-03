class treenode:
    def __init__(self,namevalue,numoccur,parentnode):
        self.name = namevalue
        self.count = numoccur
        self.nodelink = None
        self.parent = parentnode
        self.children = {}
    def inc(self,numoccur):
        self.count += numoccur
    def disp(self,ind = 1):
        print('  '*ind,self.name,' ',self.count)
        for child in self.children.values():
            child.disp(ind+1)
def createtree(dataset,minsup = 1):
    headertable = {}
    #第一遍遍历原始数据集
    for trans in dataset:
        for item in trans:
            headertable[item] = headertable.get(item,0)+dataset[trans]
    for k in list(headertable.keys()):
        #删除掉没有满足最小支持度的元素项
        if headertable[k]<minsup:
            del(headertable[k])
    freitemset = set(headertable.keys())
    if len(freitemset) == 0: return None, None
    for k in headertable:
        headertable[k] = [headertable[k],None]
    rettree = treenode('Null Set',1,None)
    #第二遍遍历原始数据集，构建FP树
    for transet,count in dataset.items():
        locald = {}#locald为排序后的频率项集
        for item in transet:
            if item in freitemset:
                locald[item] = headertable[item][0]
        if len(locald)>0:
            ordereditems = [v[0] for v in sorted(locald.items(),key = lambda p:p[1],reverse=True)]
            updateTree(ordereditems,rettree,headertable,count)
    return rettree,headertable


def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:  # check if orderedItems[0] in retTree.children
        inTree.children[items[0]].inc(count)  # incrament count
    else:  # add items[0] to inTree.children
        inTree.children[items[0]] = treenode(items[0], count, inTree)
        if headerTable[items[0]][1] == None:  # update header table
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:  # call updateTree() with remaining ordered items
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)


def updateHeader(nodeToTest, targetNode):  # this version does not use recursion
    while (nodeToTest.nodelink != None):  # Do not use recursion to traverse a linked list!
        nodeToTest = nodeToTest.nodelink
    nodeToTest.nodelink = targetNode
def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat

def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict
#插入的顺序不同，生成的BST（二叉查找树）也不同
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key

        self.payload = val  #payload为其所包含的数据项，既与键值所关联的一对数据
        self.leftChild = left
        self.rightChild = right
        self.parent = parent   #parent是用来指向其父节点的，方便后面回溯的操作。若不用此方法，也可以用一个堆栈来处理

        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    #判断是否拥有左子节点
    def hasLeftChild(self):
        return self.leftChild
    #判断是否拥有右子节点
    def hasRightChild(self):
        return self.rightChild
    #判断其是不是其父节点的左子节点
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    # 判断其是不是其父节点的右子节点
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    #判断是否是根节点
    def isRoot(self):
        return not self.parent
    #判断是否是叶子节点
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
        return not (self.rightChild or leftChild)
    #判断是否有任何子节点
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    #判断是否同时有左右子节点
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    #将键、值、左子节点、右子节点的值都更换一遍
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
def put(self,key,val):
    if self.root:
        self._put(key,val,self.root)
    else:
        self.root = TreeNode(key,val)
    self.size = self.size + 1
#put辅助方法
# 如果key比currentNode小，那么_put到左子树，但如果没有左子树，那么key就成为当前节点的左子节点
# 如果key比currentNode大，那么_put到右子树，但如果没有右子树，那么key就成为当前节点的右子节点
def _put(self,key,val,currentNode):
    if key < currentNode.key:
        if currentNode.hasLeftChild():
            self._put(key,val,currentNode.leftChild) #递归左子树
        else:
            currentNode.leftChild = TreeNode(key,val,parent=currentNode)
    else:
        if currentNode.hasRightChild():
            self._put(key,val,currentNode.rightChild)  #递归右子树
        else:
            currentNode.rightChild = TreeNode(key,val,parent=currentNode)
#索引赋值
def __setitem__(self,k,v):
    self._put(k,v)
#查找建对应的值
def get(self,key):
    if self.root:
        res = self._get(key, self.root)   #递归函数_get()
        if res:
            return res.payload     #找到节点
        else:
            return None
    else:
        return None
def _get(self,key,currentNode):
    if not currentNode:
        return None
    elif currentNode.key == key:
        return currentNode            #如果currentNode是我们要找的，则返回这个值
    elif key < currentNode.key:       #如果我们要找的key小于currentNode，则返回该节点的左子树来进行递归
        return self._get(key,currentNode.leftChild)
    else:                             #如果我们要找的key大于currentNode，则返回该节点的右子树来进行递归
        return self._get(key,currentNode.rightChild)
#索引的取值
def __getitem__(self,key):            #python内置的一种特殊的方法，对用python中的get方法
    return self.get(key)
#索引的归属判断
def __contains__(self,key):           #python内置的一种特殊的方法，对应python中的in操作符
    if self.get(key,self.root):
        return True
    else:
        return False
#迭代器，我们可以用for循环来枚举字典中的所有的key
#已中序遍历的顺序来迭代
def __iter__(self):                  #python内中的一种特殊的方法，直接调用TreeNode中的同名方法
    if self:                         #根节点不是为空的话
        if self.hasLeftChild():      #当左子树不为空
            for elem in self.leftChild:
                yield elem           #迭代器中，得用yield语句，来返回一个值
        yield self.key
        if self.hasRightChild():
            for elem in self.rightChild:
                yield elem
#删除
#用_get找到要删除的节点，然后调用remove来删除，找不到的话则提示错误
#注意：在delete中，最复杂的就是找到key对应的节点之后的remove节点的方法！
    #因为在remove一个节点之后，还要求任然保持BST的性质
def delete(self,key):
    if self.size > 1:
        nodeToRemove = self._get(key,self.root)
        if nodeToRemove:
            self.remove(nodeToRemove)
            self.size = self.size - 1
        else:
            raise KeyError('Error,key not in tree')
    elif self.size == 1 and self.root.key == key:
        self.root = None
        self.size = self.size - 1
    else:
        raise KeyError('Error,key not in tree')

def __delitem__(self,key):          #python内置的特殊方法，来调用delete()
    self.delete(key)

def remove(self,currentNode):
#情况1，待删除节点没有子节点,也就是只有一个叶子节点
    if currentNode.isLeaf():
        if currentNode == currentNode.parent.leftChild:
            currentNode.parent.leftChild = None
        else:
         currentNode.parent.rightChild = None
#情况2，待删除节点中有两个节点remove方法
    elif currentNode.hasBothChildren():
        succ = currentNode.findSuccessor()
        succ.spliceOut()
        currentNode.key = succ.key
        currentNode.payload = succ.payload
#情况3，待删除节点只有一个子节点
  #具体情况  1.被删的节点的子节点是左还是右子节点？ 2.被删节点的本身是其父节点的左还是右子节点？  3.被删的节点是根节点吗？
    #解决：将这个唯一的子节点上移，替换掉被删节点的位置
    else:
        if currentNode.hasLeftChild():
            if currentNode.isLeftChild():
                currentNode.leftChild.parent = currentNode.parent
                currentNode.parent.leftChild = currentNode.leftChild
            elif currentNode.isRightChild():
                currentNode.leftChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.leftChild
            else:
             currentNode.replaceNodeData(currentNode.leftChild.key,
                                        currentNode.leftChild.payload,
                                        currentNode.leftChild.leftChild,
                                        currentNode.leftChild.rightChild)
        else:
            if currentNode.isLeftChild():
                currentNode.rightChild.parent = currentNode.parent
                currentNode.parent.leftChild = currentNode.rightChild
            elif currentNode.isRightChild():
                currentNode.rightChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.rightChild
            else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                        currentNode.rightChild.payload,
                                        currentNode.rightChild.leftChild,
                                        currentNode.rightChild.rightChild)
#寻找后继节点
def findSuccessor(self):
    succ = None
    if self.hasRightChild():
        succ = self.rightChild.findMin()
    else:
        if self.parent:
            if self.isLeftChild():
                succ = self.parent
            else:
                self.parent.rightChild = None
                succ = self.parent.findSuccessor()
                self.parent.rightChild = self
    return succ

def findMin(self):
    current = self
    while current.hasLeftChild():
        current = current.LeftChild
    return current
def spliceOut(self):
    if self.isLeaf():
        if self.isLeftChild():
            self.parent.leftChild = None
        else:
            self.parent.rightChild = None
    elif self.hasAnyChildren():
        if self.hasLeftChild():
            if self.isLeftChild():
                self.parent.leftChild = self.leftChild
            else:
                self.parent.rightChild = self.leftChild
            self.leftChild.parent = self.parent
        else:
            if self.isLeftChild():
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
            self.rightChild.parent = self.parent


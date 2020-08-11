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


#put辅助方法
# 如果key比currentNode小，那么_put到左子树，但如果没有左子树，那么key就成为当前节点的左子节点
# 如果key比currentNode大，那么_put到右子树，但如果没有右子树，那么key就成为当前节点的右子节点
def _put(self,key,val,currentNode):
    if key < currentNode.key:
        if currentNode.hasLeftChild():
            self._put(key,val,currentNode,leftChild) #递归左子树
        else:
            currentNode.leftChild = TreeNode(key,val,parent=currentNode)
    else:
        if currentNode.hasRightChild():
            self._put(key,val,currentNode,rightChild)  #递归右子树
        else:
            currentNode.rightChild = TreeNode(key,val,parent=currentNode)

#索引赋值
def __setitem__(self,k,v):
    self._put(k,v)

#查找建对应的值
def get(self,key):
    if self.root:
        res = self._get(key, self.root)
        if res:
            return res.payload
        else:
            return None
    else:
        return None

def _get(self,key,currentNode):
    if not currentNode:
        return None
    elif currentNode.key == key:
        return currentNode
    elif key < currentNode.key:
        return self._get(key,currentNode.leftChild)
    else:
        return self._get(key,currentNode.rightChild)

def __getitem__(self,key):
    return self.get(key)

def __contains__(self,key):
    if self.get(key,self.root):
        return True
    else:
        return False

#迭代器
def __iter__(self):
    if self:
        if self.hasLeftChild():
            for elem in self.leftChild:
                yield elem
        yield self.key
        if self.hasRightChild():
            for elem in self.rightChild:
                yield elem


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

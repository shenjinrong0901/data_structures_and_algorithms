#二叉堆
class BinHeap:
    # 创建一个二叉堆
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # percUp方法
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    # 向二叉堆中添加新元素
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    # percDown方法
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.headList[i] > self.headList[mc]:
                temp = self.headList[i]
                self.headList[i] = self.headList[mc]
                self.headList[mc] = temp
            i = mc

    # minChild方法
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.headList[i * 2] < self.headList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # 从二叉堆中删除最小的元素
    def delMin(self):
        retval = self.heapList[1]     #移走堆顶
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)      #新顶下沉
        return retval

#EP67
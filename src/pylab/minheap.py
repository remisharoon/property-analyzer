
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.buildHeap(array)

    def buildHeap(self, array):
        self.heap = array
        for i in range(0, len(array)):
            self.siftUp(i, self.heap)

    def siftDown(self, currentIdx, heap):
        firstChildIdx, secondChildIdx = self.getChildrenIndices(currentIdx, heap)
        if firstChildIdx >= len(self.heap) and secondChildIdx >= len(heap):
            # reached leaf node
            return
        elif firstChildIdx < len(heap) and secondChildIdx < len(heap):
            if heap[firstChildIdx] < heap[secondChildIdx]:
                self.swapNodes(currentIdx, firstChildIdx, heap)
                self.siftDown(firstChildIdx, heap)
            else:
                self.swapNodes(currentIdx, secondChildIdx, heap)
                self.siftDown(secondChildIdx, heap)
        elif firstChildIdx < len(heap):
            if heap[currentIdx] > heap[firstChildIdx]:
                self.swapNodes(currentIdx, firstChildIdx, heap)
                self.siftDown(firstChildIdx, heap)
        elif secondChildIdx < len(heap):
            if heap[currentIdx] > heap[secondChildIdx]:
                self.swapNodes(currentIdx, secondChildIdx, heap)
                self.siftDown(secondChildIdx, heap)

    def siftUp(self, currentIdx, heap):
        if currentIdx == 0:
            return # reached root node
        parent_idx = self.getParentIdx(currentIdx, heap)
        if heap[parent_idx] > heap[currentIdx]:
            self.swapNodes(parent_idx, currentIdx, heap)
            self.siftUp(parent_idx, heap)

    def peek(self):
        return self.heap[0]

    def remove(self):
        head = self.heap[0]
        maxlen = len(self.heap) - 1
        tail = self.heap[maxlen]
        self.heap[0] = tail
        self.heap = self.heap[0:maxlen]
        self.siftDown(0, self.heap)
        return head

    def insert(self, value):
        heap_len = len(self.heap)
        self.heap.append(value)
        self.siftUp(heap_len, self.heap)

    def getParentIdx(self, nodeIdx, heap):
        return (nodeIdx - 1) // 2

    def getChildrenIndices(self, nodeIdx, heap):
        firstChildIdx = nodeIdx * 2 + 1
        secondChildIdx = firstChildIdx + 1
        return firstChildIdx, secondChildIdx

    def swapNodes(self, idx1, idx2, heap):
        temp = heap[idx1]
        heap[idx1] = heap[idx2]
        heap[idx2] = temp

arr = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]
mh = MinHeap(arr)
print(mh.heap)
mh.insert(-8)
print(mh.heap)
print(mh.remove())
print(mh.heap)
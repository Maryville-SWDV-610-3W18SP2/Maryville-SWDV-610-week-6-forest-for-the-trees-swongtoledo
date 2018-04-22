## Combined the first 2 assignments

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        
        while i // 2 > 0:
            
            if self.heapList[i] < self.heapList[i // 2]:
                
            
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,k):
        
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        
        while (i * 2) <= self.currentSize:
            
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        
        if i * 2 + 1 > self.currentSize:
            
            return i * 2
        else:
            
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1



    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
            

    def isEmpty(self):
        if currentSize == 0:
            return True
        else:
            return False

## Question number 1 answer. 
def insertOnebyOne():
    #example list 
    #list = 9,6,5,2,3
    
    bin = BinHeap()
    bin.insert(9)
    print (bin.heapList)
    bin.insert(6)
    print (bin.heapList)
    bin.insert(5)
    print (bin.heapList)
    bin.insert(2)
    print (bin.heapList)
    bin.insert(3)
    print (bin.heapList)



## Question number 2 answer. 
def insertAsList():
    bin = BinHeap()
    list = [9,6,5,2,3]
    bin.buildHeap(list)
    print (bin.heapList)



## functions to execute
#insertOnebyOne()
insertAsList()
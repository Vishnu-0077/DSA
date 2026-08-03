class BinaryHeap:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [0]*capacity

    def parent(self, i): #if i is the position of child
        return (i-1)//2
    
    def left(self,i): #if i is the position of parent
        return 2*i+1
    
    def right(self,i): #if i is the position os parent
        return 2*i+2
    
    def insert(self,val):
        if self.size == self.capacity:
            print('overflow')
            return 
         # Place new element at the end
        self.arr[self.size] = val
        k = self.size  # index of inserted element
        self.size += 1

        # Bubble up to fix min-heap property
        while k != 0 and self.arr[self.parent(k)] > self.arr[k]:
            self.arr[self.parent(k)], self.arr[k] = self.arr[k], self.arr[self.parent(k)]
            k = self.parent(k)
    
    def heapify(self,ind): #we are gonna heapify it only at that specific position, let ind be the index of the parent
        li = self.left(ind)
        ri = self.right(ind)
        smallest = ind

        if li < self.size  and self.arr[li] < self.arr[smallest]:
            smallest = li
        if ri < self.size and self.arr[ri] < self.arr[smallest]:
            smallest = ri
        if smallest != ind:
            self.arr[smallest], self.arr[ind] = self.arr[ind], self.arr[smallest]
            self.heapify(smallest) #when we want to fix whatever is below it
    
    def get_min(self):
        if self.size == 0:
            return float('inf')
        return self.arr[0]
    
    def extract_min(self): #extract the minimum value in the heap and after removing the value fix the heap
        if self.size<=0:
            return float('inf')
        if self.size ==1:
            return self.arr[0]
        min = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        self.size -= 1

        self.heapify(0)
        return min
    
    def decrease_key(self,i,val): # decrease the value at i to val and fix the heap
        if val > self.arr[i]:
            return
        self.arr[i] = val
        #  self.heapify(i) ------ we can use this if we want to arrange the elements below the index(child) but we also want to fix the parents unfortunately......
        while i!=0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)], self.arr[i] = self.arr[i], self.arr[self.parent(i)]
            i = self.parent(i)
        # why did we take care only of the parent, because if we decrease a value then value is going to move up if we want to correct, but the heapify function will only correct whatever was below it

    def delete(self,i):
        self.decrease_key(i,float('inf'))
        self.extract_min()

    def print_heap(self):
        for i in range(self.size):
            print(self.arr[i],end=" ")
        print()

if __name__ == "__main__":
    h = BinaryHeap(20)
    h.insert(4)
    h.insert(1)
    h.insert(2)
    h.insert(6)
    h.insert(7)
    h.insert(3)
    h.insert(8)
    h.insert(5)

    print("Min value is", h.get_min())  # should be 1
    h.insert(-1)
    print("Min value is", h.get_min())  # should be -1
    h.decrease_key(3, -2)  # update element at index 3
    print("Min value is", h.get_min())  # should be -2
    h.extract_min()
    print("Min value is", h.get_min())  # should be -1
    h.delete(0)
    print("Min value is", h.get_min())  # should be 1



        
    
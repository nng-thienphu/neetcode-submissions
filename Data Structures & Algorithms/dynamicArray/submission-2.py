class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity # Array of capacity = 2

    # get the value at index i-th
    def get(self, i: int) -> int:
        if i < self.length: 
            return self.arr[i] 

    # set number n at index i-th
    def set(self, i: int, n: int) -> None:
        if i < self.length: 
            self.arr[i] = n 
            return
    
    # insert element n to the end of the array
    def pushback(self, n: int) -> None:
        if self.length == self.capacity: 
            self.resize()

        self.arr[self.length] = n 
        self.length += 1  

    # return the last element and remove it
    def popback(self) -> int:
        if self.length > 0: 
            self.length -= 1
            return self.arr[self.length]

    # create a new array with double size, copy paste the element
    def resize(self) -> None:
        self.capacity = self.capacity*2
        newArr = [0] * self.capacity

        for i in range(self.length): 
            newArr[i] = self.arr[i]
    
        self.arr = newArr
    
    # number of elements
    def getSize(self) -> int:
        return self.length
    
    # capacity of array
    def getCapacity(self) -> int:
        return self.capacity

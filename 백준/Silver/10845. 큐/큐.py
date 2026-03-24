import sys
input = sys.stdin.readline

n = int(input())

class MyQueue:
    
    def __init__(self, capacity):
        self.arr = [0] * capacity
        self.head = 0
        self.tail = 0
        self._size = 0
        self.capacity = capacity
    
    def push(self, x):
        self.arr[self.tail] = int(x)
        self.tail = (self.tail + 1) % self.capacity
        self._size += 1
    
    def pop(self):
        if self._size == 0:
            return -1
        val = self.arr[self.head]
        self.head = (self.head + 1) % self.capacity
        self._size -= 1
        return val
    
    def size(self):
        return self._size
    
    def empty(self):
        return 1 if self._size == 0 else 0
    
    def front(self):
        if self._size == 0:
            return -1
        return self.arr[self.head]
    
    def back(self):
        if self._size == 0:
            return -1
        return self.arr[(self.tail - 1) % self.capacity]

que = MyQueue(n)
for i in range(n):
    output = list(input().split())
    msg = output[0]
    
    if msg == 'push':
        que.push(output[1])
    elif msg == 'pop':
        print(que.pop())
    elif msg == 'size':
        print(que.size())
    elif msg == 'empty':
        print(que.empty())
    elif msg == 'front':
        print(que.front())
    elif msg == 'back':
        print(que.back())
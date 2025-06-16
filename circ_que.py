class queue:
    def __init__(self, size):
        self.size = size
        self.list1 = [0 for i in range(size)]
        self.rear = -1
        self.front = -1


    def push(self, item):
        if self.rear == self.size - 1:
            print("Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.size
        self.list1[self.rear]=item
        self.front = 0

    def pop(self):
        if self.front == -1:
            print("Queue Underflow")
            return -1
        item = self.list1[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        self.front = (self.front + 1) % self.size
        return item

st = queue(10)
st.push(10)
st.push(50)
st.push(40)
st.push(20)
st.push(30)
print(st.pop())



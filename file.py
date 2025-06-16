class stack:
    def __init__(self, size):
        self.size = size
        self.list1 = []  
        self.top = -1

    def push(self, item):
        if self.top == self.size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.list1.append(item)  

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return -1
        item = self.list1.pop()  
        self.top -= 1
        return item

st = stack(10)
st.push(10)
st.push(50)
st.push(40)
st.push(20)
st.push(30)
st.push(70)

print(st.pop())

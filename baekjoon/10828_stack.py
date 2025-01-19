import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, i):
        self.stack.append(i)

    def pop(self):
        return -1 if not self.stack else self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if not self.stack else 0

    def top(self):
        return -1 if not self.stack else self.stack[-1]

N = int(sys.stdin.readline())
st = Stack()

for i in range(N):
    s = sys.stdin.readline().split()
    if s[0] == "top":
        print(st.top())
    elif s[0] == "empty":
        print(st.empty())
    elif s[0] == "size":
        print(st.size())
    elif s[0] == "pop":
        print(st.pop())
    elif s[0].startswith("push"):
        st.push(int(s[1]))


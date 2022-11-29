class Stack:
    def __init__(self, MaxSize):
        self.maxsize = MaxSize
        self.data = [0] * MaxSize
        self.top = 0

    def push(self, elem):
        if self.top < self.maxsize:
            self.data[self.top] = elem
            self.top += 1
            print('ok')
        else:
            self.data.append(0)
            self.data[self.top] = elem
            self.top += 1
            print('ok')
            
    def exec(self):
        if self.top == 0:
            print('error')
        else:
            print(self.data[self.top-1])
            self.data[self.top-1] = 0
            self.top -= 1

    def back(self):
        if self.top == 0:
            print('error')
        else:
            print(self.data[self.top-1])

    def size(self):
        print(self.top)

    def clear(self):
        self.data = [0] * self.maxsize
        self.top = 0
        print('ok')

    def exit(self):
        print('bye')
        return False


stack = Stack(2)
end = True
while end:
    com = input()
    if 'push' in com:
        stack.push(elem = int(com.split()[-1]))
    elif com == 'pop':
        stack.exec()
    elif com == 'back':
        stack.back()
    elif com == 'size':
        stack.size()
    elif com == 'clear':
        stack.clear()
    elif com == 'exit':
        end = stack.exit()

class Queue:
    def __init__(self, end):
        self.end = end
        self.data = [0] * end
        self.top = 0
        self.mark = 0

    def push(self, elem):
        self.data.append(elem)
        self.top += 1
        print('ok')
            
    def popq(self):
        if self.top - self.mark == 0:
            print('error')
        else:
            print(self.data[self.mark])
            self.data[self.mark] = 0
            self.mark += 1
            

    def front(self):
        if self.top - self.mark == 0:
            print('error')
        else:
            print(self.data[self.mark])

    def size(self):
        print(self.top - self.mark)

    def clear(self):
        self.data = [0] * self.end
        self.top = 0
        self.mark = 0
        print('ok')

    def test(self):
        print(self.data, '\nmark = ', self.mark, '\ntop = ', self.top, sep = '')


queue = Queue(0)
while True:
    com = input()
    if 'push' in com:
        queue.push(elem = int(com.split()[-1]))
    elif com == 'pop':
        queue.popq()
    elif com == 'front':
        queue.front()
    elif com == 'size':
        queue.size()
    elif com == 'clear':
        queue.clear()
    elif com == 'exit':
        print('bye')
        break
    elif com == 't':
        queue.test()
        

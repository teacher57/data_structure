

class Cell:

	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

	def change(self, index, com):
		if com == 'next':
			self.next = index
		elif com == 'prev':
			self.prev = index

	def give(self, com):
		if com == 'value':
			return self.value
		elif com == 'next':
			return self.next
		elif com == 'prev':
			return self.prev

class Deque:

	def __init__(self):
		self.data = []
		self.head = None
		self.tail = None
		self.size = 0
		self.length = 0

	def test(self):
		if self.size != 0:
			go = self.tail
			while True:
				print(self.data[go].give('value'), end = ' ')
				if self.data[go].give('next') == None:
					break
				else:
					go = self.data[go].give('next')
		print(end = '\n')
		print('head =', self.head, 'tail =', self.tail)
		print('size =', self.size, 'length =', self.length)
		print('size == length', self.size == self.length)

	def push_front(self, value):
		self.data.append(Cell(value))
		if self.head == None:
			self.head = 0
			self.tail = 0
			self.length += 1 # Повышаем указатели
			self.size += 1
			print('ok')
			return 0
		self.data[-1].change(self.head, 'prev') # Меняем индекс предыдущего в новом
		self.data[self.head].change(self.length, 'next') # Меняем следующий элемент у элемента, который раньше являлся головой
		self.head = self.length # Меняем указатель на голову
		self.length += 1 # Повышаем указатели
		self.size += 1
		print('ok')

	def push_back(self, value):
		self.data.append(Cell(value))
		if self.head == None:
			self.head = 0
			self.tail = 0
			self.length += 1 # Повышаем указатели
			self.size += 1
			print('ok')
			return 0
		self.data[-1].change(self.tail, 'next') # Меняем индекс следующего в новом
		self.data[self.tail].change(self.length, 'prev') # Меняем предыдущий элемент у элемента, который раньше являлся хвостом
		self.tail = self.length # Меняем указатель на хвост
		self.length += 1 # Повышаем указатели
		self.size += 1
		print('ok')

	def pop_front(self):
		if self.size == 0:
			print('error')
			return 0
		elif self.size == 1:
			print(self.data[self.head].give('value'))
			self.data = []
			self.head = None
			self.tail = None
			self.size = 0
			self.length = 0
			return 0
		print(self.data[self.head].give('value'))
		self.data[self.data[self.head].give('prev')].change(None, 'next')
		self.head = self.data[self.head].give('prev')
		self.size -= 1

	def pop_back(self):
		if self.size == 0:
			print('error')
			return 0
		elif self.size == 1:
			print(self.data[self.tail].give('value'))
			self.data = []
			self.head = None
			self.tail = None
			self.size = 0
			self.length = 0
			return 0
		print(self.data[self.tail].give('value'))
		self.data[self.data[self.tail].give('next')].change(None, 'prev')
		self.tail = self.data[self.tail].give('next')
		self.size -= 1

	def print_front(self):
		if self.size == 0:
			print('error')
			return 0
		print(self.data[self.head].give('value'))

	def print_back(self):
		if self.size == 0:
			print('error')
			return 0
		print(self.data[self.tail].give('value'))

	def print_size(self):
		print(self.size)

	def clear(self):
		self.data = []
		self.head = None
		self.tail = None
		self.size = 0
		self.length = 0
		print('ok')



def main(D = Deque()):
	while True:
		com = input()
		if 'push' in com:
			if 'push_front' in com:
				D.push_front(int(com.split()[1]))
			elif 'push_back' in com:
				D.push_back(int(com.split()[1]))
		elif com == 'pop_front':
			D.pop_front()
		elif com == 'pop_back':
			D.pop_back()
		elif com == 'front':
			D.print_front()
		elif com == 'back':
			D.print_back()
		elif com == 'size':
			D.print_size()
		elif com == 'clear':
			D.clear()
		elif com == 'exit':
			print('bye')
			break
		elif com == 't':
			D.test()

main()

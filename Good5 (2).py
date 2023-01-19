class Queue:
    def __init__(self, size): #Создание очереди с ее началом и концом
        self.queue = [None] * size
        self.tail = 0

    def enqueue(self, item):
        if self.tail < len(self.queue): 
            self.queue[self.tail] = item
            self.tail += 1
        else:
            print("Очередь переполнена")

    def dequeue(self):
        if self.tail != 0:
            item = self.queue[self.tail]
            self.tail -= 1
            return item
        else:
            print("Очередь пустая")

    def display(self):
        print(self.queue[:self.tail])

# Создание новой очереди с указанием размера
q = Queue(5)

# Добавление новых элементов в очередь
q.enqueue(1)
q.enqueue(7)
q.enqueue(3)
q.enqueue(8)

# Вывод очереди в консоль
q.display() 

# Удаление элемента из очереди
q.dequeue()
q.dequeue()

# Вывод очереди в консоль после изменений
q.display()
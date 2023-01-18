class Node:
    def __init__(self, data):
        self.data = data  # Здесь мы храним данные узла
        self.next = None  # Ссылка на следующий узел

class LinkedList:
    def __init__(self):
        self.head = None # Начало списка
    
    def add_at_beginning(self, data):
        # Создаем новый узел
        new_node = Node(data)
        # Указываем что новый узел ссылается на старое начало
        new_node.next = self.head
        # Новый узел становится началом списка
        self.head = new_node

    def add_at_end(self, data):
        # Создаем новый узел
        new_node = Node(data)
        # Если список пустой, то новый узел становится началом списка
        if self.head is None:
            self.head = new_node
            return
        # Иначе ищем последний узел
        last = self.head
        while last.next:
            last = last.next
        # Добавляем новый узел в конец списка
        last.next = new_node

    def remove_from_beginning(self):
        # Если список пустой, то ничего не делаем
        if self.head is None:
            return
        # Иначе начало списка ссылается на следующий узел
        self.head = self.head.next

    def remove_from_end(self):
        # Если список пустой, то ничего не делаем
        if self.head is None:
            return
        # Если в списке всего один элемент, то очищаем список
        if self.head.next is None:
            self.head = None
            return
        # Иначе ищем предпоследний узел
        last = self.head
        while last.next.next:
            last = last.next
        # Удаляем последний узел
        last.next = None
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next    

llist = LinkedList()
llist.add_at_beginning(1)
llist.add_at_end(2)
llist.add_at_end(3)
llist.add_at_end(4)
print("Linked list before removing from beginning:")
llist.print_list()
llist.remove_from_beginning()
print("\nLinked list after removing from beginning:")
llist.print_list()
llist.remove_from_end()
print("\nLinked list after removing from end:")
llist.print_list()




# 10.	Разработать программу для работы с линейным односвязным списком, 
# позволяющую добавлять элемент в начало и в конец списка, а также удалять элемент из начала и из конца списка.
# Предусмотреть вывод списка на экран.
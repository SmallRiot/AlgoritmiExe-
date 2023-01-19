class Node:
    def __init__(self, data):
        # конструктор класса Node, инициализирует данные и следующий элемент.
        # Принимает на вход данные, которые будут храниться в элементе списка.
        self.data = data
        # инициализирует ссылку на следующий элемент списка как None.
        self.next = None

class LinkedList:
    def __init__(self):
        # конструктор класса LinkedList, инициализирует начало списка.
        # Создаёт пустой список.
        self.head = None

    def add_to_beginning(self, data):
        # метод, добавляющий элемент в начало списка.
        # Принимает на вход данные, которые будут храниться в добавляемом элементе.
        new_node = Node(data)
        # делает следующим элементом добавляемого элемента первый элемент списка.
        new_node.next = self.head
        # делает добавляемый элемент первым элементом с-писка.
        self.head = new_node


    def reverse(self):
        # метод, реверсирующий список.
        prev = None
        current = self.head
        # идёт по списку до тех пор, пока текущий элемент не равен None.
        while(current is not None):
            # сохраняет ссылку на следующий элемент в переменную next.
            next = current.next
            # меняет направление ссылки текущего элемента на предыдущий элемент.
            current.next = prev
            # сдвигает предыдущий элемент на текущий.
            prev = current
            # сдвигает текущий элемент на следующий.
            current = next
    # делает последний обработанный элемент новым началом списка.
        self.head = prev

    def print_list(self):
        # метод, выводящий список на печать.
        # использует временную переменную temp для прохода по списку.
        temp = self.head
        # идёт по списку до тех пор, пока temp не равен None.
        while(temp):
            # выводит данные текущего элемента.
            print(temp.data)
            # сдвигает temp на следующий элемент.
            temp = temp.next
    


linked_list = LinkedList()
linked_list.add_to_beginning(1)
linked_list.add_to_beginning(2)
linked_list.add_to_beginning(3)
print("Original List:")
linked_list.print_list()
linked_list.reverse()
print("Reversed List:")
linked_list.print_list()

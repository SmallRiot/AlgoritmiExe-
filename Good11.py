class Node:
    def __init__(self, data):
        # конструктор класса Node, инициализирует данные и следующий элемент
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # конструктор класса LinkedList, инициализирует начало списка
        self.head = None

    def add_to_beginning(self, data):
        # метод, добавляющий элемент в начало списка
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        # метод, реверсирующий список
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def print_list(self):
        # метод, выводящий список на печать
        temp = self.head
        while(temp):
            print(temp.data)
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

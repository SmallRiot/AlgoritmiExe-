class Node:
    def __init__(self, data):
        self.data = data # данные узла
        self.next = None # ссылка на следующий узел

class LinkedList:
    def __init__(self):
        self.head = None # начало списка

    def add_node(self, data):
        new_node = Node(data) 
        if self.head is None: # если список пустой
            self.head = new_node # добавляем новый узел в начало
            return
        current = self.head
        if self.head.data >= data: # вот эта дурацкая проверка для первого элемментра, чтобы их менять, без нее первый эллемент будет неизменным (- час моей работы, АААА)
            new_node.next = self.head
            self.head = new_node
            return
        while current.next and current.next.data <= data: # ищем место для добавления узла
            current = current.next
        new_node.next = current.next # вставляем узел
        current.next = new_node


    def print_list(self):
        current = self.head
        while current: # проходим по списку
            print(current.data) # выводим данные узла
            current = current.next

llist = LinkedList()
llist.add_node(3)
llist.add_node(1)
llist.add_node(9)
llist.add_node(4)
llist.add_node(5)
llist.add_node(2)

llist.print_list()

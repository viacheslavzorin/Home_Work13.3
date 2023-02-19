class Node:
    """ Это узел """
    def __init__(self, data, next = None):
        self.data = data  # тут данные
        self.next = next # тут ссылка на следующий

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """ Тут добавление элемента """
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)
print(n2.data)
print(n1)
print(n2.next)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next.data)
print(stack.top.next.next.data)
#print(stack.top.next.next.next)
print(stack.top.next.next.next)


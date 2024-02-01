class node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
    def show(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
link = linkedlist()
e1 = node('1')
link.head = e1
link.show()
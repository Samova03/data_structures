from utils.print_utils import print_arabic

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = QueueNode(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def enqueue_at_position(self, data, position):
        new_node = QueueNode(data)
        if position == 0:
            new_node.next = self.front
            self.front = new_node
            if not self.rear:
                self.rear = new_node
            return
        
        temp = self.front
        count = 0
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        
        if temp is None:
            print_arabic("الموضع غير صالح!")
            return
        
        new_node.next = temp.next
        temp.next = new_node
        if new_node.next is None:
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print_arabic("الطابور فارغ!")
            return
        self.front = self.front.next
        if not self.front:
            self.rear = None

    def dequeue_at_position(self, position):
        if self.front is None:
            print_arabic("الطابور فارغ!")
            return
        
        if position == 0:
            self.front = self.front.next
            if not self.front:
                self.rear = None
            return
        
        temp = self.front
        count = 0
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        
        if temp is None or temp.next is None:
            print_arabic("الموضع غير صالح!")
            return
        
        temp.next = temp.next.next
        if temp.next is None:
            self.rear = temp

    def display(self):
        if self.front is None:
            print_arabic("الطابور فارغ!")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

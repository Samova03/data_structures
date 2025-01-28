from utils.print_utils import print_arabic

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def push_at_position(self, data, position):
        new_node = StackNode(data)
        if position == 0:
            new_node.next = self.top
            self.top = new_node
            return
        temp = self.top
        count = 0
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        if not temp:
            print_arabic("الموضع غير صالح!")
            return
        new_node.next = temp.next
        temp.next = new_node

    def pop(self):
        if self.top is None:
            print_arabic("المكدس فارغ!")
            return
        self.top = self.top.next

    def pop_at_position(self, position):
        if self.top is None:
            print_arabic("المكدس فارغ!")
            return
        if position == 0:
            self.top = self.top.next
            return
        temp = self.top
        count = 0
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        if not temp or not temp.next:
            print_arabic("الموضع غير صالح!")
            return
        temp.next = temp.next.next

    def display(self):
        if self.top is None:
            print_arabic("المكدس فارغ!")
            return
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

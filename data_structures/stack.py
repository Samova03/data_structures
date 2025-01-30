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
        if position < 0 or position > self.size():
            print_arabic("الموضع غير صالح!")
            return
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
        new_node.next = temp.next
        temp.next = new_node

    def pop(self):
        if self.top is None:
            print_arabic("المكدس فارغ!")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def pop_at_position(self, position):
        if position < 0 or position >= self.size():
            print_arabic("الموضع غير صالح!")
            return None
        if position == 0:
            return self.pop()
        temp = self.top
        count = 0
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        popped_data = temp.next.data
        temp.next = temp.next.next
        return popped_data

    def size(self):
        temp = self.top
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def peek(self):
        if self.top is None:
            print_arabic("المكدس فارغ!")
            return None
        return self.top.data
   
    def display(self):
        if self.top is None:
            print_arabic(" المكدس فارغ ")
            return
        temp = self.top
        print_arabic(" محتويات المكدس:")
        while temp:
            print_arabic(f"  [{temp.data}]")
            temp = temp.next
        print_arabic("   (TOP)")

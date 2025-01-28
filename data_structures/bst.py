from utils.print_utils import print_arabic

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  

class ArabicBST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
            print_arabic(f"تم إنشاء الجذر: {value}")
            return
        
        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = BSTNode(value)
                    current.left.parent = current
                    print_arabic(f"تم إضافة {value} ← يسار {current.value}")
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = BSTNode(value)
                    current.right.parent = current
                    print_arabic(f"تم إضافة {value} → يمين {current.value}")
                    break
    
    def visualize_arabic(self, node=None, level=0, prefix='الجذر: '):
        if node is None:
            node = self.root
            if not node:
                print_arabic("الشجرة فارغة!")
                return
        
        if node.right:
            self.visualize_arabic(node.right, level + 1, 'يمين: ')
        
        print('    ' * level + '└── ' + prefix + str(node.value))
        
        if node.left:
            self.visualize_arabic(node.left, level + 1, 'يسار: ')
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None:
            print_arabic(f"العنصر {value} غير موجود")
            return None
        if node.value == value:
            print_arabic(f"تم العثور على {value}")
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if not node:
            return node
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left:
                temp = node.right
                print_arabic(f"تم حذف {value}")
                return temp
            elif not node.right:
                temp = node.left
                print_arabic(f"تم حذف {value}")
                return temp
            
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def to_sorted_list(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)
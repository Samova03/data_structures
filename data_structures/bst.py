# استيراد الدالة print_arabic من وحدة utils.print_utils
from utils.print_utils import print_arabic

# تعريف فئة العقدة في شجرة البحث الثنائية
class BSTNode:
    def __init__(self, value):
        # قيمة العقدة
        self.value = value
        # المؤشر إلى العقدة اليسرى
        self.left = None
        # المؤشر إلى العقدة اليمنى
        self.right = None
        # المؤشر إلى العقدة الأب (ليس ضروريًا في بعض التطبيقات)
        self.parent = None  

# تعريف فئة شجرة البحث الثنائية باللغة العربية
class ArabicBST:
    def __init__(self):
        # الجذر الابتدائي للشجرة
        self.root = None
    
    # دالة لإدراج قيمة جديدة في الشجرة
    def insert(self, value):
        # إذا كانت الشجرة فارغة، يتم إنشاء الجذر بالقيمة
        if not self.root:
            self.root = BSTNode(value)
            print_arabic(f"تم إنشاء الجذر: {value}")
            return
        
        # بدء البحث عن الموضع المناسب لإدراج القيمة
        current = self.root
        while True:
            # إذا كانت القيمة المراد إدراجها أقل من قيمة العقدة الحالية، نتجه إلى اليسار
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    # إدراج العقدة في الفرع الأيسر
                    current.left = BSTNode(value)
                    current.left.parent = current
                    print_arabic(f"تم إضافة {value} ← يسار {current.value}")
                    break
            else:
                # إذا كانت القيمة أكبر أو تساوي، نتجه إلى اليمين
                if current.right:
                    current = current.right
                else:
                    # إدراج العقدة في الفرع الأيمن
                    current.right = BSTNode(value)
                    current.right.parent = current
                    print_arabic(f"تم إضافة {value} → يمين {current.value}")
                    break
    
    # دالة لتصور الشجرة باستخدام تنسيق نصي باللغة العربية
    def visualize_arabic(self, node=None, level=0, prefix='الجذر: '):
        # إذا لم يتم تمرير عقدة، نبدأ من الجذر
        if node is None:
            node = self.root
            # إذا كانت الشجرة فارغة
            if not node:
                print_arabic("الشجرة فارغة!")
                return
        
        # أولاً، نقوم بعرض الفرع الأيمن (لأن القراءة من الأعلى إلى الأسفل في اللغة العربية)
        if node.right:
            self.visualize_arabic(node.right, level + 1, 'يمين: ')
        
        # طباعة العقدة الحالية مع تباعد حسب مستوى العقدة
        print('    ' * level + '└── ' + prefix + str(node.value))
        
        # عرض الفرع الأيسر
        if node.left:
            self.visualize_arabic(node.left, level + 1, 'يسار: ')
    
    # دالة للبحث عن قيمة في الشجرة
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    # دالة بحث باستخدام الاستدعاء الذاتي (التكرار الذاتي)
    def _search_recursive(self, node, value):
        # إذا وصلت إلى نهاية الشجرة دون العثور على القيمة
        if node is None:
            print_arabic(f"العنصر {value} غير موجود")
            return None
        # إذا تم العثور على العقدة التي تحتوي على القيمة
        if node.value == value:
            print_arabic(f"تم العثور على {value}")
            return node
        # إذا كانت القيمة أقل، البحث في الفرع الأيسر
        if value < node.value:
            return self._search_recursive(node.left, value)
        # وإلا البحث في الفرع الأيمن
        return self._search_recursive(node.right, value)
    
    # دالة لحذف قيمة من الشجرة
    def delete(self, value):
        # تحديث الجذر بعد الحذف (لأن الجذر قد يتغير)
        self.root = self._delete_recursive(self.root, value)
    
    # دالة حذف باستخدام الاستدعاء الذاتي
    def _delete_recursive(self, node, value):
        # إذا لم يتم العثور على العقدة
        if not node:
            return node
        
        # البحث عن القيمة في الفرع الأيسر
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        # البحث عن القيمة في الفرع الأيمن
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # حالة حذف العقدة التي ليس لها فرع أيسر
            if not node.left:
                temp = node.right
                print_arabic(f"تم حذف {value}")
                return temp
            # حالة حذف العقدة التي ليس لها فرع أيمن
            elif not node.right:
                temp = node.left
                print_arabic(f"تم حذف {value}")
                return temp
            
            # إذا كانت العقدة تحتوي على فرعين:
            # إيجاد أقل قيمة في الفرع الأيمن (العقدة البديلة)
            temp = self._min_value_node(node.right)
            # استبدال قيمة العقدة الحالية بقيمة العقدة البديلة
            node.value = temp.value
            # حذف العقدة البديلة من الفرع الأيمن
            node.right = self._delete_recursive(node.right, temp.value)
        
        return node
    
    # دالة لإيجاد العقدة التي تحتوي على أقل قيمة في شجرة فرعية
    def _min_value_node(self, node):
        current = node
        # الانتقال إلى أقصى اليسار للحصول على أقل قيمة
        while current.left:
            current = current.left
        return current
    
    # دالة لتحويل الشجرة إلى قائمة مرتبة باستخدام الترتيب الوسيط (inorder)
    def to_sorted_list(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    # دالة الترتيب الوسيط (inorder traversal) لإضافة القيم إلى القائمة
    def _inorder_traversal(self, node, result):
        if node:
            # المرور على الفرع الأيسر
            self._inorder_traversal(node.left, result)
            # إضافة قيمة العقدة الحالية إلى القائمة
            result.append(node.value)
            # المرور على الفرع الأيمن
            self._inorder_traversal(node.right, result)

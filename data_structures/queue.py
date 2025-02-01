# استيراد الدالة print_arabic من وحدة utils.print_utils
from utils.print_utils import print_arabic

# تعريف فئة عقدة الطابور
class QueueNode:
    def __init__(self, data):
        # تخزين البيانات في العقدة
        self.data = data
        # المؤشر إلى العقدة التالية في الطابور
        self.next = None

# تعريف فئة الطابور
class Queue:
    def __init__(self):
        # المؤشر إلى بداية الطابور
        self.front = None
        # المؤشر إلى نهاية الطابور
        self.rear = None

    # دالة لإضافة عنصر إلى نهاية الطابور (enqueue)
    def enqueue(self, data):
        # إنشاء عقدة جديدة تحمل البيانات
        new_node = QueueNode(data)
        # إذا كان الطابور فارغًا، يكون العنصر الجديد هو البداية والنهاية
        if not self.rear:
            self.front = self.rear = new_node
            return
        # ربط العقدة الجديدة بنهاية الطابور وتحديث المؤشر rear
        self.rear.next = new_node
        self.rear = new_node

    # دالة لإدراج عنصر في موضع محدد داخل الطابور
    def enqueue_at_position(self, data, position):
        # إنشاء عقدة جديدة تحمل البيانات
        new_node = QueueNode(data)
        # إذا كان الموضع هو البداية (0)
        if position == 0:
            new_node.next = self.front
            self.front = new_node
            # إذا كان الطابور فارغًا، يتم تحديث المؤشر rear أيضًا
            if not self.rear:
                self.rear = new_node
            return
        
        # التنقل في الطابور للوصول إلى الموضع المناسب للإدراج
        temp = self.front
        count = 0
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        
        # إذا لم يكن الموضع صالحًا (خارج نطاق الطابور)
        if temp is None:
            print_arabic("الموضع غير صالح!")
            return
        
        # ربط العقدة الجديدة بالعقد التالية وإدراجها في الطابور
        new_node.next = temp.next
        temp.next = new_node
        # إذا تمت الإضافة في نهاية الطابور، تحديث المؤشر rear
        if new_node.next is None:
            self.rear = new_node

    # دالة لإزالة العنصر من بداية الطابور (dequeue)
    def dequeue(self):
        # التحقق من كون الطابور فارغًا
        if self.front is None:
            print_arabic("الطابور فارغ!")
            return
        # إزالة العقدة الأولى بتحديث المؤشر front
        self.front = self.front.next
        # إذا أصبح الطابور فارغًا بعد الإزالة، يتم تحديث المؤشر rear
        if not self.front:
            self.rear = None

    # دالة لإزالة عنصر من موضع محدد داخل الطابور
    def dequeue_at_position(self, position):
        # التحقق من كون الطابور فارغًا
        if self.front is None:
            print_arabic("الطابور فارغ!")
            return
        
        # إذا كان الموضع هو البداية (0)
        if position == 0:
            self.front = self.front.next
            # تحديث المؤشر rear إذا أصبح الطابور فارغًا
            if not self.front:
                self.rear = None
            return
        
        # التنقل في الطابور للوصول إلى العنصر السابق للعنصر المطلوب إزالته
        temp = self.front
        count = 0
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        
        # إذا كان الموضع غير صالح (خارج نطاق الطابور)
        if temp is None or temp.next is None:
            print_arabic("الموضع غير صالح!")
            return
        
        # إزالة العقدة المحددة من خلال تخطيها وربط العقدة السابقة بالعقدة التالية
        temp.next = temp.next.next
        # إذا تمت الإزالة من نهاية الطابور، تحديث المؤشر rear
        if temp.next is None:
            self.rear = temp

    # دالة لعرض عناصر الطابور
    def display(self):
        # التحقق من كون الطابور فارغًا
        if self.front is None:
            print_arabic("الطابور فارغ!")
            return
        # التنقل في الطابور وعرض البيانات في كل عقدة
        temp = self.front
        while temp:
            # طباعة البيانات مع فاصل يوضح التسلسل بين العقد
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        # الانتقال للسطر التالي بعد العرض
        print()

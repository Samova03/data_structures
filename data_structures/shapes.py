# استيراد الدالة print_arabic من وحدة utils.print_utils لعرض النصوص باللغة العربية
from utils.print_utils import print_arabic

# تعريف فئة الشكل الأساسي (الشكل الأب)
class Shape:
    def __init__(self, color="أسود"):
        # تهيئة لون الشكل مع قيمة افتراضية "أسود"
        self.color = color 
    
    # دالة لحساب مساحة الشكل
    # يجب أن تُنفذ هذه الدالة في الفئات الفرعية الخاصة بكل شكل
    def area(self):
        raise NotImplementedError("يجب تنفيذ هذه الدالة في الفئة الفرعية")
    
    # دالة لتغيير أبعاد الشكل (تغيير الحجم)
    # يجب أن تُنفذ هذه الدالة في الفئات الفرعية الخاصة بكل شكل
    def resize(self, factor):
        raise NotImplementedError("يجب تنفيذ هذه الدالة في الفئة الفرعية")
    
    # دالة لعرض معلومات الشكل الأساسية
    def display_info(self):
        print_arabic(f"معلومات الشكل - اللون: {self.color}")

# تعريف فئة المستطيل التي ترث من فئة Shape
class Rectangle(Shape):
    def __init__(self, color, width, height):
        # استدعاء مُنشئ الفئة الأم لتعيين اللون
        super().__init__(color)
        # تعيين عرض وارتفاع المستطيل
        self.width = width
        self.height = height
    
    # تنفيذ دالة حساب مساحة المستطيل
    def area(self):
        return self.width * self.height
    
    # تنفيذ دالة تغيير أبعاد المستطيل
    # يمكن تغيير الحجم بنفس النسبة لكلا البعدين أو بنسب مختلفة
    def resize(self, factor, factor2=None):
        if factor2 is None:
            # تغيير كلا الأبعاد بنفس النسبة
            self.width *= factor
            self.height *= factor
            print_arabic(f"تم تغيير الأبعاد بنسبة {factor}")
        else:
            # تغيير العرض والارتفاع بنسب مختلفة
            self.width *= factor
            self.height *= factor2
            print_arabic(f"تم تغيير العرض بنسبة {factor} والارتفاع بنسبة {factor2}")
    
    # دالة لتحويل بيانات المستطيل إلى سلسلة نصية عند طباعته
    def __str__(self):
        return f"مستطيل - اللون: {self.color}، الأبعاد: {self.width}x{self.height}"

# تعريف فئة الدائرة التي ترث من فئة Shape
class Circle(Shape):
    def __init__(self, color, radius):
        # استدعاء مُنشئ الفئة الأم لتعيين اللون
        super().__init__(color)
        # تعيين نصف قطر الدائرة
        self.radius = radius
    
    # تنفيذ دالة حساب مساحة الدائرة باستخدام تقريب قيمة π
    def area(self):
        return 3.14 * self.radius ** 2
    
    # تنفيذ دالة تغيير حجم الدائرة عن طريق تغيير نصف القطر
    def resize(self, factor):
        self.radius *= factor
        print_arabic(f"تم تغيير نصف القطر بنسبة {factor}")
    
    # دالة لتحويل بيانات الدائرة إلى سلسلة نصية عند طباعتها
    def __str__(self):
        return f"دائرة - اللون: {self.color}، نصف القطر: {self.radius}"

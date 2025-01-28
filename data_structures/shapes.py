from utils.print_utils import print_arabic

class Shape:
    def __init__(self, color="أسود"):
        self.color = color
    
    def area(self):
        raise NotImplementedError("يجب تنفيذ هذه الدالة في الفئة الفرعية")
    
    def resize(self, factor):
        raise NotImplementedError("يجب تنفيذ هذه الدالة في الفئة الفرعية")
    
    def display_info(self):
        print_arabic(f"معلومات الشكل - اللون: {self.color}")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def resize(self, factor, factor2=None):
        if factor2 is None:
            self.width *= factor
            self.height *= factor
            print_arabic(f"تم تغيير الأبعاد بنسبة {factor}")
        else:
            self.width *= factor
            self.height *= factor2
            print_arabic(f"تم تغيير العرض بنسبة {factor} والارتفاع بنسبة {factor2}")
    
    def __str__(self):
        return f"مستطيل - اللون: {self.color}، الأبعاد: {self.width}x{self.height}"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def resize(self, factor):
        self.radius *= factor
        print_arabic(f"تم تغيير نصف القطر بنسبة {factor}")
    
    def __str__(self):
        return f"دائرة - اللون: {self.color}، نصف القطر: {self.radius}"
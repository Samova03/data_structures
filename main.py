import sys
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.bst import ArabicBST
from data_structures.shapes import Rectangle, Circle
from utils.user_input import get_valid_integer
from utils.print_utils import print_arabic

def main():
    stack = Stack()
    queue = Queue()
    bst = ArabicBST()
    shapes = []

    while True:
        print_arabic("\n-----------------------------------------")
        print_arabic("الخيارات الرئيسية:")
        print_arabic("1. مكدس")
        print_arabic("2. طابور")
        print_arabic("3. شجرة بحث ثنائية")
        print_arabic("4. أشكال هندسية")
        print_arabic("5. خروج")
        print_arabic("-----------------------------------------")
        print_arabic("أدخل اختيارك: ")
        choice = input().strip()

        if choice == "1":
            handle_stack(stack)
        
        elif choice == "2":
            handle_queue(queue)
        
        elif choice == "3":
            handle_bst(bst)
        
        elif choice == "4":
            handle_shapes(shapes)
        
        elif choice == "5":
            print_arabic("وداعًا!")
            sys.exit()
        
        else:
            print_arabic("اختيار غير صحيح! حاول مرة أخرى.")

def handle_stack(stack):
    while True:
        print_arabic("\n--- المكدس ---")
        print_arabic("\nاختر عملية:")
        print_arabic("1. إضافة عنصر")
        print_arabic("2. إضافة عنصر في موضع")
        print_arabic("3. حذف عنصر")
        print_arabic("4. حذف عنصر من موضع")
        print_arabic("5. عرض المحتويات")
        print_arabic("6. العودة")
        print_arabic("أدخل اختيارك: ")
        op = input().strip()

        if op == "1":
            print_arabic("أدخل العنصر: ")
            data = input()
            stack.push(data)
        
        elif op == "2":
            print_arabic("أدخل العنصر: ")
            data = input()
            print_arabic("أدخل الموضع: ")
            pos = get_valid_integer("")
            stack.push_at_position(data, pos)
        
        elif op == "3":
            stack.pop()
        
        elif op == "4":
            print_arabic("أدخل الموضع: ")
            pos = get_valid_integer("")
            stack.pop_at_position(pos)
        
        elif op == "5":
            stack.display()
        
        elif op == "6":
            break
        
        else:
            print_arabic("خيار غير صحيح!")

def handle_queue(queue):
    while True:
        print_arabic("\n--- الطابور ---")
        print_arabic("\nاختر عملية:")
        print_arabic("1. إضافة عنصر")
        print_arabic("2. إضافة عنصر في موضع")
        print_arabic("3. حذف عنصر")
        print_arabic("4. حذف عنصر من موضع")
        print_arabic("5. عرض المحتويات")
        print_arabic("6. العودة")
        print_arabic("أدخل اختيارك: ")
        op = input().strip()

        if op == "1":
            print_arabic("أدخل العنصر: ")
            data = input()
            queue.enqueue(data)
        
        elif op == "2":
            print_arabic("أدخل العنصر: ")
            data = input()
            print_arabic("أدخل الموضع: ")
            pos = get_valid_integer("")
            queue.enqueue_at_position(data, pos)
        
        elif op == "3":
            queue.dequeue()
        
        elif op == "4":
            print_arabic("أدخل الموضع: ")
            pos = get_valid_integer("")
            queue.dequeue_at_position(pos)
        
        elif op == "5":
            queue.display()
        
        elif op == "6":
            break
        
        else:
            print_arabic("خيار غير صحيح!")

def handle_bst(bst):
    while True:
        print_arabic("\n--- شجرة البحث الثنائية ---")
        print_arabic("\nاختر عملية:")
        print_arabic("1. إضافة عنصر")
        print_arabic("2. بحث عن عنصر")
        print_arabic("3. حذف عنصر")
        print_arabic("4. عرض الشجرة")
        print_arabic("5. عرض العناصر مرتبة")
        print_arabic("6. العودة")
        print_arabic("أدخل اختيارك: ")
        op = input().strip()

        if op == "1":
            print_arabic("أدخل العنصر: ")
            data = input()
            bst.insert(data)
        
        elif op == "2":
            print_arabic("أدخل العنصر للبحث: ")
            data = input()
            bst.search(data)
        
        elif op == "3":
            print_arabic("أدخل العنصر للحذف: ")
            data = input()
            bst.delete(data)
        
        elif op == "4":
            bst.visualize_arabic()
        
        elif op == "5":
            sorted_list = bst.to_sorted_list()
            print_arabic("العناصر المرتبة: " + " ← ".join(sorted_list))
        
        elif op == "6":
            break
        
        else:
            print_arabic("خيار غير صحيح!")

def handle_shapes(shapes):
    while True:
        print_arabic("\n--- الأشكال الهندسية ---")
        print_arabic("\nاختر عملية:")
        print_arabic("1. إنشاء مستطيل")
        print_arabic("2. إنشاء دائرة")
        print_arabic("3. تعديل حجم")
        print_arabic("4. عرض المعلومات")
        print_arabic("5. حساب المساحات")
        print_arabic("6. العودة")
        print_arabic("أدخل اختيارك: ")
        op = input().strip()

        if op == "1":
            print_arabic("أدخل اللون: ")
            color = input()
            print_arabic("أدخل العرض: ")
            width = get_valid_integer("")
            print_arabic("أدخل الارتفاع: ")
            height = get_valid_integer("")
            shapes.append(Rectangle(color, width, height))
            print_arabic("✓ تم إنشاء المستطيل بنجاح")
        
        elif op == "2":
            print_arabic("أدخل اللون: ")
            color = input()
            print_arabic("أدخل نصف القطر: ")
            radius = get_valid_integer("")
            shapes.append(Circle(color, radius))
            print_arabic("✓ تم إنشاء الدائرة بنجاح")
        
        elif op == "3":
            if not shapes:
                print_arabic("⚠ لا توجد أشكال!")
                continue
            print_arabic("الأشكال المتوفرة:")
            for i, s in enumerate(shapes):
                print_arabic(f"{i+1}. {s}")
            try:
                idx = int(input("اختر الرقم: ")) - 1
                selected = shapes[idx]
                
                if isinstance(selected, Rectangle):
                    print_arabic("معامل العرض: ")
                    f1 = float(input())
                    print_arabic("معامل الارتفاع (اختياري): ")
                    f2 = input().strip()
                    if f2:
                        selected.resize(f1, float(f2))
                    else:
                        selected.resize(f1)
                else:
                    print_arabic("معامل التغيير: ")
                    f = float(input())
                    selected.resize(f)
                
                print_arabic("✓ تم التعديل بنجاح")
            except:
                print_arabic("⚠ حدث خطأ في الإدخال!")
        
        elif op == "4":
            if not shapes:
                print_arabic("⚠ لا توجد أشكال لعرضها!")
                continue
            print_arabic("معلومات الأشكال:")
            for s in shapes:
                s.display_info()
        
        elif op == "5":
            if not shapes:
                print_arabic("⚠ لا توجد أشكال!")
                continue
            print_arabic("النتائج:")
            for i, s in enumerate(shapes):
                print_arabic(f"الشكل {i+1}: {s.area():.2f}")
        
        elif op == "6":
            break
        
        else:
            print_arabic("خيار غير صحيح!")

if __name__ == "__main__":
    main()

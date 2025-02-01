from .print_utils import print_arabic

def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print_arabic("يرجى إدخال عدد صحيح!") 
import arabic_reshaper
from bidi.algorithm import get_display

def print_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    print(bidi_text)
from deep_translator import GoogleTranslator
from bidi.algorithm import get_display
import arabic_reshaper

# path is our file that we intend to translator
# output is our translator language
# we put the text of our desired file in the text variable to translate it in the output variable

path = "D:/work_python/motarjem/Chapter_1.txt"
file = open(path , encoding="utf8")
text = file.read()
output = GoogleTranslator(source="en",target="fa").translate(text)

# the def function is for Arabic and Persian texts that do not have a culttered
def convert(output):
    reshaped_text = arabic_reshaper.reshape(output)
    converted = get_display(reshaped_text)
    return converted

print(convert(output))


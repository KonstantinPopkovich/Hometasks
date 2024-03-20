#Во входной строке записан текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
def count_words (a):
     a = str(a)
     b = a.split()
     c = set(b)
     return len(c)
d = ("Hello, my name is Konstantin. Hello, my name is Kirill. How are you today? I'm fine,thank you"
     )
e = count_words(d)
print(f"The number of words is {e}")
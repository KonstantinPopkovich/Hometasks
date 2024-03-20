#Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
#Учитывать только английские буквы.


a = input("Write the sentence:")
upper = 0
lower = 0
for i in a:
    if 'A' <= i <= 'Z':
        upper += 1
    elif 'a' <= i <= 'z':
        lower += 1

print("The number of upper letters is", b)
print("The number of lower letters is", c)

#
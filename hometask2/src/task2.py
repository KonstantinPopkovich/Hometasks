#Найти самое длинное слово в введенном предложении.
#Учтите что в предложении есть знаки препинания.
#Подсказки:
#my_string.split([chars]) возвращает список строк.
#len(list) - количество элементов в списке

a = str(input("Enter the sentence:"))
b = a.split(" " or "," or ";")
c = max(b, key=len)
print("The biggest word in the sentence is", c)
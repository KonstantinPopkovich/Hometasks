#Вводится строка.
#Требуется удалить из нее повторяющиеся символы и все пробелы.
#Например, если было введено "abc cde def", то должно быть выведено "abcdef".


a = input("Enter the sentence:")
b = ""
for i in a:
    if i not in b and i != " ":
        b += i
print(b)

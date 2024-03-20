#Создайте словарь из строки 'pythonist' следующим образом:
# в качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.

def letter_count_dict(string):
    letter_count = {}
    for letter in string:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count
string = 'pythonist'
result_dict = letter_count_dict(string)
print(result_dict)
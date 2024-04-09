#Написать функцию которая определяет читается ли слово с двух концов одинаково
# True если да False если нет. Решить наиболее оптимальным путем.


def palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(palindrome("MOUSuom"))
#Написать функцию которая принимает 2 слова и проверяет являются ли они анограммами друг друга.
#True если да False если нет. Решить наиболее оптимальным путем.


def anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

print(anagrams("Taxi", "Ixat"))

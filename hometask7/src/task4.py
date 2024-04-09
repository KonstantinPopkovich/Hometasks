#Есть список слов аннограмм ["asd", "dsa", "tar", "rat", "bla"]
# сгруппировать аннограммы к такому виду [["asd", "dsa], ["tar", "rat"], ["bla"]]
# - допустимая сложность алгоритма O(n)
def groups_of_anagrams(words):
    groups = {}
    for word in words:
        word_hash = 0
        for char in word:
            word_hash += ord(char)
        if word_hash in groups:
            groups[word_hash].append(word)
        else:
            groups[word_hash] = [word]

    return list(groups.values())

word_list = ["asd", "dsa", "tar", "rat", "bla"]
print(groups_of_anagrams(word_list))
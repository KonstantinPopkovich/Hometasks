#Создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), полученный объект dict_items передайте в написанную вами функцию,
# которая создает и возвращает новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями – числа.

def dictionary(dict):
    reversed_dictionary = {}
    for key, value in dict.items():
        reversed_dictionary[value] = key
    return reversed_dictionary

dict = {1:"one", 2:"two", 3:"three"}

reversed_dictionary_result = dictionary(dict)
print(reversed_dictionary_result)
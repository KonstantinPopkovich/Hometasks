#Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}.
# Объедините их в один при помощи встроенных функций языка Python.
def dict():
    dictionary_1 = {'a': 300, 'b': 400}
    dictionary_2 = {'c': 500, 'd': 600}

    dictionary_1.update(dictionary_2)
    return dictionary_1
print(dict())
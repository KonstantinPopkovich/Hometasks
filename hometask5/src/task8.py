#Даны два списка одинаковой длины.
# Необходимо создать из них словарь таким образом, чтобы элементы первого списка были ключами,
# а элементы второго — соответственно значениями нашего словаря.

def dict_from_lists():
    keys_list = ["a", "b", "c"]
    values_list = range(1,4)
    return dict(zip(keys_list, values_list))
print(dict_from_lists())
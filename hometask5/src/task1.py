#Напишите функцию to_dict(lst),
# которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

def to_dict(lst):
    return {element: element for element in lst}

my_list = [1, 5, 7, 'Hello world', 'Konstantin', ("Popkovich", "Igorevich")]
a = to_dict(my_list)
print(a)
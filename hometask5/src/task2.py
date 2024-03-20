#Иван решил создать самый большой словарь в мире.
# Для этого он придумал функцию biggest_dict(**kwargs),
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict,
# состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

def the_biggest_dict(**kwargs):
    dict_1 = {"first_one": "we can do it"}

    for key, value in kwargs.items():
        dict_1[key] = value

    return dict_1

a = the_biggest_dict(second_one = "we can't do it", third_one = "we'll die!!!!!!")
print(a)
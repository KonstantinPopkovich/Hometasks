#Дана строка в виде случайной последовательности чисел от 0 до 9.
#Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
def count_it(sequence):
    num_count = {}

    for character in sequence:
        if character.isdigit():
            num = int(character)
            num_count[num] = num_count.get(num, 0) + 1

    def sort_by_value(item):
        return item[1]

    sorted_counts = sorted(num_count.items(), key=sort_by_value)
    top_3 = dict(sorted_counts[:3])
    return top_3

sequence = "12345678901234567890"
result = count_it(sequence)
print(result)
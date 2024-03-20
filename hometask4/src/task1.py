#Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20,
#а значениями кубы этих чисел.
# dictionary = {a: a**3 for a in range(1, 21)}
# print(dictionary)

def dictionary_cube():
    dictionary = {a: a ** 3 for a in range(1, 21)}
    return dictionary
b = dictionary_cube()
for n_1,n_3 in b.items():
    print(f"{n_1}: {n_3}")


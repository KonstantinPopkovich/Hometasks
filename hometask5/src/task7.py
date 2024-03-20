#Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
def dictionary_cube():
    dictionary = {a: a ** 3 for a in range(1, 11)}
    return dictionary
b = dictionary_cube()
for n_1,n_3 in b.items():
    print(f"{n_1}: {n_3}")
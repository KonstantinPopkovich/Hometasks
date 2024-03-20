#Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

def multiple_values(dict):

    a = 1
    for i in dict.values():
        a *= i
    return a

dict = {"a": 1, "b": 2, "c": 3, "d": 3, "e": 4}
multiplication = multiple_values(dict)
print(f"The result of multiplication is {multiplication}")
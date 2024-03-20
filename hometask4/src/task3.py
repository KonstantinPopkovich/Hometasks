#Даны два списка чисел.
# Посчитайте, сколько различных чисел содержится одновременно как в первом списке, так и во втором.
def count_numbers_1 (a,b):
    c = set(a)
    d = set(b)
    e = c & d
    return len(e)
a = [1,2,4,7,9,11,18,36]
b = [2,7,9,11,18,35]
f = count_numbers_1(a,b)
print(f"The number of the common unique numbers is {f} ")

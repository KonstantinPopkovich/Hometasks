#Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков
def count_numbers_2 (a,b):
    c = set(a)
    d = set(b)
    e = (c | d) - (c & d)
    return len(e)
a = [1,2,4,7,9,11,18,36]
b = [2,7,9,11,18,35]
f = count_numbers_2(a,b)
print(f"The number of the different numbers is {f} ")
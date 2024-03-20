#Даны два натуральных числа.
#Вычислите их наибольший общий делитель при помощи алгоритма Евклида
#(мы не знаем функции и рекурсию).

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
while b:
    a, b = b, a%b
print(f"The gcd is {a}")

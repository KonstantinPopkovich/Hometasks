#Даны: три стороны треугольника.
#Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь. Если нет, вывести сообщение о неверных данных.

a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))
d = 0.5 * (a+b+c)
if a+b>c and b+c>a and c+a>b:
    S = (d * (d-a) * (d-b) * (d-c)) ** 0.5
    print ("The area of this triangle is", S)
else:
    print("That's not a triangle!")
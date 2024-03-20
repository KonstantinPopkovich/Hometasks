#Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
#Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)

#a = input("Enter the number:")
#a = str(a)
#if a == a[::-1]:
 #   print("That's palindrome")
#else:
 #   print("That's not palindrome")

a = int(input("Enter the number: "))
b = 0
c = a
while a > 0:
  b = b * 10 + a % 10
  a = a // 10
if c == b:
  print("That's palindrome")
else:
  print("That's not palindrome")

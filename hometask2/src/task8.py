#Требуется сложить два целых числа А и В.

#a = 2
#b = 3
#print (a+b)

#Услуги телефонной сети оплачиваются по следующему правилу:
# за разговоры до А минут в месяц – В рублей за минуту,
# а разговоры сверх установленной нормы оплачиваются из расчета С рублей за минуту.
# Требуется написать программу,
# вычисляющую плату за пользование телефоном для разговоров продолжительностью Т минут в месяц.

#a = int(input("Enter the amount of minutes:"))
#b = 0
#if a<120:
#    b = 1
#else:
  #  b = 2
  #  print(a*b)

#Маша и Миша собирали землянику.
# Маше удалось сорвать X ягод, а Мише – Y ягод.
# Поскольку ягода была очень вкусной, то ребята могли какую-то часть ягод съесть.
# По нашим подсчетам вместе они съели Z ягод.
#Требуется определить: сколько ягод ребята собрали в результате, при этом следует проверить,
# не ошиблись ли мы в расчетах, подсчитывая количество съеденных ягод
# (их не должно было получиться больше, чем сорванных ягод).

#a = int(input("Masha picked "))
#b = int(input("Misha picked "))
#c = int(input("They ate"))
#d = a + b - c
#if d<0:
 #   print("Something wrong")
#else:
 #   print(d)

#Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#a = int(input("Enter the number"))
#b = (a / 6) * 2
#c = a - b
#print("Boys made", b)
#print("Girl made", c)


#If we list all the natural numbers below 1$ that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#a = 0
#for b in range(1000):
  #  if b % 3 == 0 or b % 5 == 0:
   #     a += b
    #    print(a)
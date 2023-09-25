a = 5
b = 5
c = 7

if a + b < c or b + c < a or a + c < b:
    print('Не существует')
elif a == b and a == c and b == c:
    print('Равносторонний')
elif a == b or a == c or b == c:
    print('Равнобедренный')
else:
    print('Разносторонний')


a = 5
b = 9
c = 10

if (b < a < c or c < a < b) and (a % 3 == 0 and a % 2 == 0):
    print("Среднее:", a)
elif (a < b < c or c < b < a) and (b % 3 == 0 and b % 2 == 0):
    print("Среднеее:", b)
elif (a < c < b or b < c < a) and (c % 3 == 0 and c % 2 == 0):
    print("Среднее:", c)
else:
    print("Ошибка")
if (a < b and a < c) and (a % 2 == 0 and a > 1):
    print("Минимальное:", a)
elif (b < a and b < c) and (b % 2 == 0 and b > 1):
    print("Минимальное:", b)
elif (c < a and c < b) and (c % 2 == 0 and c > 1):
    print("Минимальное:", c)
else:
    print("Число меньше 1 и нечетное")
if (a > b and a > c) and (((b + c) // 2) < a or (b * с) > a):
    print("Максимальное:", a)
elif (b > a and b > c) and (((a + c) // 2) < b or (a * c) > b):
    print("Максимальное:", b)
elif (c > a and c > b) and (((a + b) // 2) < c) or (a * b > c):
    print("Максимальное:", c)
else:
    print("Error")



a = 1997
if a % 4 == 0 and a % 100 != 0:
    print("Високосный")
elif a % 4 == 0 and a % 400 == 0:
    print("Високосный")
else:
    print("Не високосный")


m = 90
w = 1.83
a = 27
IMT = m / (w ** 2)
if (IMT < 22 and a >= 45) or (IMT < 18.5 and a < 45):
    print(IMT, "Недостаточная масса тела")
if (22 < IMT < 26.99 and a >= 45) or (18.5 < IMT < 24.99 and a < 45):
    print(IMT, "Норма")
if (27 < IMT < 31.99 and a >= 45) or (25 < IMT < 29.99 and a < 45):
    print(IMT, "Избыточная масса тела")
if (IMT >= 32 and a >= 45) or (IMT >= 30 and a < 45):
    print(IMT, "Ожирение")

from collections import Counter
c = Counter("123456789123")
dict (c.most_common())

input_str = input()
output_str = ""
for number in input_str:
  output_str += str(abs(9-int(number)))
print(output_str)

lst_in = [4,5,7,22,90]
st_out = ""
for elem in lst_in:
  st_out += str(elem)
print(st_out)

a = int(input())
b = int(input())
c = int(input())

while True:
  if b-a == c-b:
    print("ok")
    break

dct = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
st = int(input("Введите число"))
print(dct.get(st, "День недели не найден"))

try:
  A = float(input("Введите А:"))
  B = float(input("Введите В:"))
except ValueError() as e:
  print(f"Ошибка: {e}")
if (A == 1) and (B == 1):
  print("Решение-любое число")
if (A==0) or (A==B+1):
  raise ValueError("Решения уравнений нет")
try:
  if A!=0:
    x = (B-1)/A-1
    print("Решение уравнения:", x)
except ZeroDivisionError as e :
  print(e)

try:
  A = float(input("Введите А:"))
  B = float(input("Введите В:"))
  C = float(input("Введите С:"))
except ValueError() as e:
  print(f"Ошибка: {e}")
  D = B**2 - 4*A*C
  if D >0:
    X1 = (-B+(D**0.5))/(2*A)
    X2 = (-B-(D**0.5))/(2*A)
    print(X1, X2)
  if D == 0:
    X = (-B/(2*A))
    print(X)
  if D < 0:
    raise ValueError ("Нет корней")

import math
try:
  A = float(input("Введите А:"))
except ValueError() as e:
  raise ValueError(f"Ошибка: {e}")
if A == 0:
  X = (-1)
  print (X)
else:
  try:
    X = math.sin(A)/(A*(A-1))
    print(X)
  except ZeroDivisionError() as e:
   print(e)

import random
N = 3
M = 3
matrix = [
    [random.randit(1,100)for elem in range (N)] for row in range (M)
]

matrix
max_elem = 0
for row in matrix:
  if max(row)>max_elem:
    max_elem = max(row)
print(max_elem)

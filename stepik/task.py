# i = int(input('введите '))

# # if i % 2 == 0: 
# #     print(i, 'чётное')
# # else:
# #     print(i, 'нечётное')

# # if i % 2 != 0:
# #     print(i, 'нечётное')
# # else:
# #     print(i, 'чётное')

# ////////////////////////////
# Напишите программу, которая проверяет,
# что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.

# a = int(input('введите число'))
# print(a)
# if a//1000+a%10 == (a//100%10 - a//10%10):
#     print('Да')
# else: 
#     print('Нет')
#//////2 вариант
# a,b,c,d = input()
# print('ДА' if int(a) + int(d) == int(b) - int(c) else 'НЕТ')
#//////////////////////////////////////
# Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.
# Формат входных данных:
# На вход программе подаётся целое число — возраст пользователя.
# Формат выходных данных:
# Программа должна вывести текст «Доступ разрешен» если возраст не менее 18, и «Доступ запрещен» в противном случае.
# a = int(input())  # 1 вариант
# if a >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')
#////////////
# print('Доступ разрешен' if  int(input()) >= 18 else 'Доступ запрещен')
#///////////////////////////////
#Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке)
# последовательными членами арифметической прогрессии.
# a,b,c = int(input()),int(input()),int(input()),
# x = b-a
# y = c-b
# if  x==y:
#     print('YES')
# else:
#     print('NO')
#//////////
# a, b, c = int(input()), int(input()), int(input())
# if b - a == c - b:
#     print('YES')
# else:
#     print('NO')
#///////////////////////////////
# Напишите программу, которая определяет наименьшее из двух чисел.
# a,b = int(input()),int(input())
# if a > b :
#    print(b)
# else:
#    print(a)                   
#/////
#         print(min(int(input()), int(input())))   
#Напишите программу, которая определяет наименьшее из четырёх чисел.
#  print(min(int(input()), int(input()),int(input()), int(input())))  1 вариант
#     a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a > b:
#     a = b
# if c > d:
#     c = d
# if a > c:
#     a = c
# print(a)    2 вариант
#/////////////////
#a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a < b < c < d:
#     print (a)
# else:
#     if b < c < d:
#         print (b)
#     else:
#         if c < d:
#             print (c)
#         else:
#             print (d)
#//////////////////////////////
# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.
# a =int(input())
# if a<=13:
#     print('детство')
# if 13<a<=24:
#     print('молодость')
# if 24<a<=59:
#     print('зрелость')
# if a>=60:
#     print('старость')
#///
# age = int(input())
# if age>13:
#     if age>24:
#         if age>59:
#                 print('старость')
#         else:
#             print('зрелость')
#     else:
#         print('молодость')
# else:
#     print('детство')

# Напишите программу, которая считывает три числа и 
# подсчитывает сумму только положительных чисел.
# a,b,c=int(input()),int(input()),int(input()),
# x = 0
# if a < 0:
#     a = 0
# if b < 0:
#      b = 0
# if c < 0:
#       c = 0
# x = a+b+c

# print(x)
#///////
# a, b, c, s = int(input()), int(input()), int(input()), 0
# if a > 0:
#     s += a
# if b > 0:
#     s += b
# if c > 0:
#     s += c
# print(s)
#///////////////////
# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:
#     print('число', num1, 'выиграло')
# else:
#     print('число', num2, 'выиграло')
#/////////////////////////
# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
    
# p =  (a + b)*(a + b)
# print(p)
#/////////////////////////
# Напишите программу, которая по координатам точки,
# не лежащей на осях координат, определяет номер координатной четверти, в которой она находится.
# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')
# Напишите программу, которая принимает целое число xx и определяет, п
# ринадлежит ли данное число указанным промежуткам.
# a=int(input())
# if   -30< a <= -2 or 7< a <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')
#////
# x = int(input())
# if (x > -30 and x <= -2) or (x > 7 and x <= 25):
#     print('Принадлежит')
# else:
#     print('Не принадлежит')
# Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
# Напишите программу, определяющую, является ли введённое число красивым. 
# Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
# a =int(input())
# if  1000 <= a <= 9999 and (a%7 ==0 or (a%17) == 0)  : 
#      print('YES')
# else:
#     print('NO')
# ////
# x = int(input())
# if 1000 <= x <= 9999:
#     if x % 7 == 0 or x % 17 == 0:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")
# Високосный год
# Напишите программу, которая определяет, является ли год с данным номером високосным. Если год является високосным, то выведите «YES», иначе выведите «NO».

# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
# a = int(input())
# if a%4 == 0 and a%100!=0 or a%400==0:
#     print('YES')
# else:
#     print('NO')
# # Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.
# a,b,c = int(input()),int(input()),int(input())
# if a < c + b and b < a+c and c < b+ a:
#     print('YES')
# else:
#     print('NO')
#Даны две различные клетки шахматной доски. Напишите программу,
#которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом.
#Программа получает на вход четыре числа от 1 до 8 каждое, 
#задающие номер столбца и номер строки сначала для первой клетки,
#потом для второй клетки. Программа должна вывести «YES», 
#если из первой клетки ходом ладьи можно попасть во вторую,
#  или «NO» в противном случае.
# a1,b1,a2,b2 = int(input()),int(input()),int(input()),int(input())
# if ((a1 + 1 >= a2 or a1 - 1 <=a2) and b1 == b2) or ((b1 + 1 >= b2 or b1 - 1 <=b2) and a1 == a2) :
#     print('YES')
# else:
#     print('NO')

# Даны две различные клетки шахматной доски. 
# Напишите программу,  которая определяет, может ли король попасть с первой клетки
# на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 
# каждое, задающие номер столбца и номер строки сначала для первой клетки, 
# потом для второй клетки. Программа должна вывести «YES», 
# если из первой клетки ходом короля можно попасть во вторую, 
# или «NO» в противном случае.
# a1,b1,a2,b2 = int(input()),int(input()),int(input()),int(input())
# if (a1 +1 >= a2 and b1 + 1 >= b2) and (a1 +1 >= a2 and b1 - 1 <= b2) and (a1 - 1 <= a2 and b1 + 1 >= b2) and (a1 - 1 <= a2 and b1 - 1 <= b2):
#     print('YES')
# else:
#     print('NO')
# Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара.
#  В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир, 
#  поэтому Флэш решил не рисковать без причины, 
#  и узнать у своего друга Циско Рамона есть ли смысл принимать вызов. 
#  Циско получил данные, что скорость Зума равна nn,
#   а скорость Флэша равна kk.

# Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.
# n,k = int(input()),int(input())
# if n > k:
#     print('NO')
# elif n < k:
#     print('YES')
# else:
#     print("Don't know")

# Напишите программу, которая принимает три положительных числа
# и определяет вид треугольника, длины сторон которого равны введенным
# числам.
# a,b,c = int(input()),int(input()),int(input())
# if a == b == c:
#     print('Равносторонний')
# elif (a == b != c) or (b == c != a) or (a == c !=b):
#     print('Равнобедренный')
# else:
#     # print('Разносторонний')

# Даны три различных целых числа. Напишите программу, 
# которая находит среднее по величине число.
# a,b,c = int(input()),int(input()),int(input())
# x = b
# if ( a > b and a < c) or (a < b and a > c):
#     print(a)
# elif (b > c and b < a) or (b < c and b > a):
#     print(b)
# else:
#     print(c)
# ///////
# a, b, c = int(input()), int(input()), int(input())
# if (a - b) * (c - b) < 0:
#     print(b)
# elif (b - a) * (c - a) < 0:
#     print(a)
# else:
#     print(c)
# Количество дней
# Дан порядковый номер месяца (1, \, 2, \ldots, 12)(1,2,…, 12).
# Напишите программу, которая выводит на экран количество дней в этом месяце.
# Принять, что год является невисокосным
# a = int(input())
# if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
#     print('31')
# elif a == 2  :
#     print('28')
# elif a == 4 or a == 6 or a == 9 or a == 11:
#     print('30')
#///////
# x = int(input())

# if x == 2:
#     print(28)
# elif (x < 8 and x % 2 == 0) or (x > 7 and x % 2 != 0):
#     print(30)
# else:
# #     print(31)
# Известен вес боксера-любителя (целое число). Известно, что вес таков, 
# что боксер может быть отнесён к одной из трех весовых категорий:
# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, 
# в какой категории будет выступать данный боксер.
# a = int(input())
# if a < 60:
#     print('Легкий вес')
# elif a >= 60 and a < 64:
#     print('Первый полусредний вес')
# else:
#/////
# m = int(input())
# print('Легкий вес' if m < 60 else 'Первый полусредний вес' if m < 64 else 'Полусредний вес')
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
# Формат входных данных
# На вход программе подаётся названия трех городов, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
# Примечание. Гарантируется, что длины названий всех трех городов различны.

# name1 = input()
# name2 = input()
# name3 = input()
# long1 = len(name1)
# long2 = len(name2)
# long3 = len(name3)
# if long1 > long2 and long1 >long3 and long2 > long3:
#     print(name3,name1,sep='\n')
# elif long1 > long2 and long1 >long3 and long3 > long2:
#     print(name2,name1, sep='\n')    
# elif long2 > long1 and long2 > long3 and long1 > long3:
#     print(name3,name2,sep='\n')
# elif long2 > long1 and long2 > long3 and long3 > long1:
#     print(name1,name2,sep='\n')    
# elif long3 > long1 and long3 > long2 and long1 > long2:
#     print(name2,name3,sep='\n')
# elif long3 > long1 and long3 > long2 and long3 > long1:
#     print(name1,name3, sep='\n')   
from math import sqrt, pow
a, b = float(input()), float(input())
print((a + b) / 2)
print(sqrt(a * b))
print((2 * a * b) / (a + b))
print(sqrt((pow(a,2) + pow(b, 2)) / 2))



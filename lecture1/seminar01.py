# Напишите программу, которая принимает на вход два числа и проверяет,
#  является одно число квадратом другого
# n = int(input("Введите первое число :"))
# m = int(input("Введите второе число :"))
# if n == m**2 or m == n**2:
#     print("Yes")
# else:
#     print("No")
# напишите программу, которая на вход принимает 5 цифр
# и выдает наибольшее
# num_max = 0
# for i in range(5):
#     num = int(input())
#     if num > num_max:
#         num_max= num
# print('самое большое число', num_max)
# ///////////////////////////////
# 3. Напишите программу, которая будет на вход принимать
# число N и выводить числа от -N до 

# def range_numbers_n():
#     n = int(input("Input your number: "))
#     print(*range(-n , n + 1))

# range_numbers_n()
# //////////////////////////////////
# 4. Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.
# def check_first_num():
#    number = float(input("Введите число : "))
#    new_num = int(number * 10 % 10)
#    print(new_num)

# check_first_num()
# //////////////////////////////
# 5. Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.
# num = int(input("Введите число : "))
# if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
#     print("Yes")
# else:
#     print("No")
# //////////////////////////
# # 6. Пример проверки ложности утверждения (x ≡ z ) ∨ (x → (y ∧ z))
# print("x y z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not (x == z or x <= y and z):
#                 print(x, y, z)
#//////////////////////////////////
# нельзя присваивать переменным следующие:
# False;
# True;
# None;
# and;
# with;
# as;
# assert;
# break;
# class;
# continue;
# def;
# del;
# elif;
# else;
# except;
# finally;
# try;
# for;
# from;
# global;
# if;
# import;
# in;
# is;
# lambda;
# nonlocal;
# not;
# or;
# pass;
# raise;
# return;
# while;
# yield.
# print('Java')
# print('Ruby')
# print('Scala')
# //////////////////
# a =int(input())
# b = int(a + 1)
# c = int(b + 1)
# print(a)
# print(b)
# print(c)
# ///////////////////////
# a = int(input)
# v = int(a ** 3)
# s = int(6 * a ** 2)
# print(v)  # можно так print(f'Объем = {v})
# print(s)  # print(f"Площадь полной поверхности = {s}")
# # 3 вариант в одну строку
# # a = int(input())
# print(f'Объем = {a**3}\nПлощадь полной поверхности = {6*a**2}')
#//////////////////////////
# a = int(input())
# b = int(input())
# #print(a)
# #print(b)
# c = int(3*(a +b) **3 + 275*b**2 - 127*a - 41)
# print(c)


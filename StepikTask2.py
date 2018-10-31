# A = float(input())
# B = float(input())
# C = input()
# if C == "*":
#     print(A*B)
# elif C == "+":
#     print(A+B)
# elif C == "-":
#     print(A-B)
# elif C == "pow":
#     print(A**B)
# elif B == 0:
#     print("Деление на 0!")
# else:
#     if C == "div":
#         print(A//B)
#     elif C == "mod":
#         print(A%B)
#     elif C == "/":
#         print(A/B)

# f = input()
# if f == "прямоугольник":
#     a = float(input())
#     b = float(input())
#     print(a*b)
# elif f == "треугольник":
#     a = float(input())
#     b = float(input())
#     c = float(input())
#     p = ((a + b + c)/2)
#     s = float((p*(p-a)*(p-b)*(p-c))**0.5)
#     print(s)
# elif f == "круг":
#     r = float(input())
#     pi = 3.14
#     print(pi * (r**2))

# a, b, c = int(input()),int(input()),int(input())
# max, min = a, b
# if max <= b:
#     max = b
# if max <= c:
#     max = c
# if min >= a:
#     min = a
# if min >= c:
#     min = c
# print(max, min,((a + b + c)-(max+min)), sep ="\n")
 

# n = int(input())
# if 0 <= n <= 1000:
#     if n % 10 == 2 or n % 10 == 3 or n % 10 == 4 or n == 2 or n == 3 or n == 4:
#         if n == 12 or n == 13 or n == 14 or n % 100 == 12 or n % 100 == 13 or n % 100 == 14 :
#             print(n, "программистов")
#         else:
#             print(n, "программиста")
#     elif n % 10 == 1 or n == 1:
#         if n == 11 or n == 111 or n % 100 == 11:
#             print(n, "программистов")
#         else:
#             print(n, "программист")
#     else:
#         print(n, "программистов")

n = int(input())
a = int(n % 10)
b = int(n % 100 * 0.1)
c = int(n % 1000 * 0.01)
d = int(n % 10000 * 0.001)
e = int(n % 100000 * 0.0001)
f = int(n % 1000000 * 0.00001)
if (a + b + c) == (d + e + f):
    print("Счастливый")
else:
    print("Обычный")






# s = 0
# while s == 0:
#     n = int(input())
#     if n < 10:
#         continue
#     if n > 100:
#         break 
#     else:
#         print(n)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a <= b and c <= d and a <= 10 and b <= 10 and c <= 10 and d <= 10:
    for i in range(a, b + 1):
        for j in range(c, d + 1): 
            if i == a:
                print('\t', j, end = '\t')
        print()
        print(i, end ='') 
        for k in range(c, d + 1):
            print('\t', i * k, end = '\t') 








    # for i in range(a - 1, b + 1):
    #     if i != a - 1:
    #         print(i)
    #     else:
    #         for j in range(c, d + 1):
    #             if j == c:
    #                 print('\t', j, end = '\t')
    #             else:
    #                 print(j, end = '\t')            
    #         print()













    # for i in range(c, d + 1):
    #     print(i, end = '\t')
    #     print(' ')
    #     for j in range(a, b + 1):
    #         print(j) 
 
 
 
 
 
 
 
 
 
 


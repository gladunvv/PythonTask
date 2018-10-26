# Обращение по индексу строки
s = 'python'
print(s[0])
print(s[4])
print(s[:4])
print(s[1:4])
print(s[5:])
print(s[::-1])
print(s[::2])
# Вшитие переменных в текст
age = 10
name = 'Lisa'
print("Hello my cat's name is {a} and she is {b} years old!".format(a = name, b = age))
print('Hello my cat\'s name is ' + name +  ' and she is ' + str(age) + ' years old!')
# Замена значения в списке
l = [21, 2, [3, 12, True], [10, 13, 'Hello', False]]
l[3][2] = 'Goodbay'
print(l)
# Обращение  к словарю
d1 = {'key': 'hello'}
d2 = {'key1': {'key2': 'hello'}}
d3 = {'key1': [{'neset_key1': ['deep', ['hello']]}]}

print(d1['key'])
print(d2['key1']['key2'])
print(d3['key1'][0]['neset_key1'][1][0])
# Использование множества
my_list = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]
print(set(my_list))
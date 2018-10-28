# f = open('text.txt', 'w')
# f.write('Name Email Phone\n')
# f.write('Vladislav Gladun\n')
# f.write('BattyBoop@cartoon.com\n')
# f.write('8-800-555-35-35\n')
# f.close()

# f1 = open('text1.txt', 'w')
# f1.writelines(['klmno\n', 'vwxyz\n', 'abcde\n', 'pqrstu\n', 'fghij\n'])
# f1.close()

# f = open('text.txt', 'r')
# print(f.read())

# f = open('text.txt', 'r')
# print(f.read(1))

# f = open('text.txt', 'r')
# print(f.readline())

# f = open('text.txt', 'r')
# print(f.readlines())

# f = open('text.txt', 'r')
# f.seek(10)
# print(f.read())

# f = open('text.txt', 'r')
# for line in f:
#     print(line, end = "")


# for line in open('text.txt'):
#     print(line, end = '')

# fin = open('text1.txt', 'r')
# buf = fin.readlines()
# fin.close()
# buf.sort()
# fout = open('text2.txt', 'w')
# for line in buf:
#     fout.write(line)
#     print(line, end = "")
# fout.close()

f = open('text.txt', 'r')
content = f.read()
f.close()
words = content.split()
print(words, end ="\n")
print('There are {0} words in the file' .format(len(words)))
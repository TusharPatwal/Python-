# f = open('data.txt','r')

# # print(f.read())
# print(f.readline())

# f1 = open('abc','w')
# f1.write('buffer')
# f1.write(' laptop')

# f2 = open('abc','a')
# f2.write(' hello')


f = open('data.txt','r')

f1 = open('abc','w')

for data in f:
    f1.write(data)
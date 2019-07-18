i = 1
while i<=10:# 控制行数

    j = 0
    while j<=(10-i):
        print('*',end='')
        j = j+1
    print('')

    i = i+1

对于这种倒三角形的形式，可以采用10-i的方法，类似的可见冒泡排序

# i = 10
# while i>=0:# 控制行数

#     j = 0
#     while j<=(10-i):
#         print('*',end='')
#         j = j+1
#     print('')

#     i = i-1
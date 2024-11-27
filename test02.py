# -*- coding:utf-8 -*-
# coding=utf-8
'''
@Author: fat_joe
@Date: 2024/11/26 11:01
@Desc: 用于理解列表、字典、元祖 嵌套
        还有另外一个test03.py文件可以帮助理解
'''
tuple1 = ('a','b','c','d')
tuple2 = ('e','f','g','h')
tuple3 = ('i','j','k','l')
tuple4 = ('m','n','o','p')
dict1 = {'weizhi01':tuple1,'weizhi02':tuple2}
dict2 = {'weizhi01':tuple3,'weizhi02':tuple4}
list1 = [dict1,dict2]
# print("这是打印%s",(tuple1))
print(dict1['weizhi01'])
print(dict1['weizhi01'][2])       # 打印出来是c
print(list1[1]['weizhi02'][3])    # 打印出来是 p


#循环第一层
for i in list1:
    print(i)

# {'weizhi01': ('a', 'b', 'c', 'd'), 'weizhi02': ('e', 'f', 'g', 'h')}
# {'weizhi01': ('i', 'j', 'k', 'l'), 'weizhi02': ('m', 'n', 'o', 'p')}
print('***************************************')

#循环第二层
for i in list1:
    # print(type(i))
    # i的类型是dict
    # for j in i:
        # print (j)
        # j的类型是str
        # weizhi01
        # weizhi02
        # weizhi01
        # weizhi02
    for j in i.items():
        # print(type(j))
        # j 的类型是tuple
        print(j)  
# ('weizhi01', ('a', 'b', 'c', 'd'))
# ('weizhi02', ('e', 'f', 'g', 'h'))
# ('weizhi01', ('i', 'j', 'k', 'l'))
# ('weizhi02', ('m', 'n', 'o', 'p'))


        # print(type(j))
        # for k in j:
        #     print(k.values)

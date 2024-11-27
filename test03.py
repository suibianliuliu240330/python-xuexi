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

for i in list1:
    # print(i)
    # print('\n')
    for j in i.items():   ##这个是遍历键值对，也就是说键和值都会遍历出来。
        print(f"键=》{j[0]}")
        print(f"值=》{j[1]}")
        # 键=》weizhi01
        # 值=》('a', 'b', 'c', 'd')
        # 键=》weizhi02
        # 值=》('e', 'f', 'g', 'h')
        # 键=》weizhi01
        # 值=》('i', 'j', 'k', 'l')
        # 键=》weizhi02
        # 值=》('m', 'n', 'o', 'p')
        # print(f"值里面的元素=》"{j[1][2]})   #这个是错误的
        # print("开始遍历值中的所有元素")
        # k=0
        # while k < len(j[1]):
        #     print(j[1][k])
        #     k+=1
        #如果要是for语句不能in 数字，需要给定范围 例如使用 range（5）
        for k in range(len(j[1])):
            print(j[1][k])
            # 键=》weizhi01
            # 值=》('a', 'b', 'c', 'd')
            # a
            # b
            # c
            # d
            # 键=》weizhi02
            # 值=》('e', 'f', 'g', 'h')
            # e
            # f
            # g
            # h
            # 键=》weizhi01
            # 值=》('i', 'j', 'k', 'l')
            # i
            # j
            # k
            # l
            # 键=》weizhi02
            # 值=》('m', 'n', 'o', 'p')
            # m
            # n
            # o
            # p
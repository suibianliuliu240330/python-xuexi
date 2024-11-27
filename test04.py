# -*- coding:utf-8 -*-
# coding=utf-8
'''
@Author: fat_joe
@Date: 2024/11/27 11:05
@Desc: ...
'''

def my_function():
    """
    这里面写的是方法的解释说明，介绍这个方法是干什么用的。
    """
    # pass
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k,"=>", v)    
        
my_function()
# print(my_function.__doc__)



year = 2016
event = '哈哈哈哈哈'
print(f'这是print+f打印的：{year}{event}')
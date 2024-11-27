# -*- coding:utf-8 -*-
# coding=utf-8
'''
@Author: fat_joe
@Date: 2024/11/25 15:48
@Desc: ...
'''
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

print(users.copy())

#print(type(users.copy().items()))
print(users.copy().items())   #返回类型是个字典
####    dict_items([('Hans', 'active'), ('Éléonore', 'inactive'), ('景太郎', 'active')])

# print(users['hans'])  ##这个报错
# print(users[0])  ##这个报错
print(users[0]['Hans'])  ##这个报错




# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
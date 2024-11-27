import json
for i in range (0,5):
    print ('for:'+str(i))
    # break #只是跳出循环体
    if (i!=3):
        print ('if:'+str(i))
        continue
        print ('这是continue后面的code，当条件符合时，不应该显示出来\n')
        # 不管if条件是否符合，continue后面的语句都没有被执行，不知道为什么，后续还需要查看文档）

# print('xxxxxxxxxxx')
zidian={}
for i in range (0,6):
    zidian['姓名'+str(i)] = '王五'+str(i)

print("python中原始字典的数据格式:")
print(zidian)
print("\n\n")
p2j=json.dumps(zidian,ensure_ascii=False)
print("p2j转换后，格式是json："+p2j)

zidian1 = {'tom':2,'jim':4}

# zidian1['jim']=666 赋值
print(zidian1)
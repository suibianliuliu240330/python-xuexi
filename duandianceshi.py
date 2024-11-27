l1=[]
d1={}
i=0
for i in range(2):
    # l1[i]=d1.setdefault('name','suibianshishi','age',20) #不能超过2个参数
    d1['name']='suibianshishi'
    d1['age']='20'
    # print(d1)
    l1.append(d1)

    # print(type(l1))
    # print(l1)
print(l1[0]['name'])
print(l1[0]['age'])
l1=[]
for i in range(10):
    print(i)
    l1.append(i)
print(l1)
print(len(l1))

dic1={
    '7506E':['BJYZ002_BD_AS_14','大数据'],
    'CE12800':['BJYZ003_F03_BL_01','F03区'],
    'S5731':['BJYZ003_RT01_BMC_01','RT01区']
}

print(dic1['S5731'])
# ['BJYZ003_RT01_BMC_01', 'RT01区']
print(dic1['S5731'][0])
# BJYZ003_RT01_BMC_01

print()
print()

for k,v in dic1:
    print(f'')
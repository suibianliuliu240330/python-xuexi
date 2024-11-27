import json
l1 = [
    ['学号','姓名','班级'],
    [1,'张三','初二1班'],
    [2,'王五','初二2班'],
    [3,'李四','初二2班'],
    [4,'sssss','ffffffff']
]
# p2j=json.dumps(l1,ensure_ascii=False)
p2j=json.dumps(l1)
# 中文字符没有乱码，只是出现了反斜杠，此时解决方法应考虑是否进行了二次序列化
# 在dump时加入ensure_ascii=False 即可解决，即json.dump(json_data, f, indent=4, ensure_ascii=False)

print(type(p2j))
print(p2j)
# print(len(l1))
print(l1)
# print(l1[2:3])

f1=r'D:\20241104_py_xuexi\20241112_lx\a.txt'

f11=open(f1,'r')
# f11=open(f1,'+a')
# f11.write("通过python写入的中文内容，用于判断是否乱码。")
# f11.write("\n\n\n中文内容11111111")

print(f11.read())



f11.close()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}x{i}={i*j}", end='\t')
#     print()  # 换行

# for i in range(1,1):
#     print(f"{i}",end='\t')


for i in range(4):
    ## range(5)内容是0,1,2,3,4
    ## 第一次运行 range 为0时，i不打印。可以理解为range中数次为执行次数
    
    for j in range(i):
        print("打印的是i",i)
        print('打印的是j',j)
        print(f"j*i={(j+1)*i}",end='\t')
        print()
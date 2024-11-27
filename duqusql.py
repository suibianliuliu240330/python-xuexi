import sqlite3
from sqlite3 import Error
import xlrd

# 连接到SQLite数据库
# 数据库文件是 test.db，如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('d:\\20241104_py_xuexi\\20241112_lx\\shebeiliebiao.db')
# print(conn)
# 创建一个Cursor:
cursor = conn.cursor() #使用sql的话需要创建游标对象
# 执行查询语句，查询steudent表的所有数据:
# cursor.execute('SELECT * FROM student')
# values = cursor.fetchall()
# print(type(values))
# print(values)

data=xlrd.open_workbook('d:\\20241104_py_xuexi\\20241112_lx\\设备列表_test.xls')

#获取sheet中的内容，暂时只获取第一个sheet中的内容
table_0 = data.sheets()[0]
#获取行数和列数
nor = table_0.nrows
nol = table_0.ncols
#获取表头信息，为一个列表
header_row_data_0 = table_0.row_values(0)

#现获取sheet1中的内容

i=0
#编列结果是list，然后在进行嵌套字典
shebeiliebiao = [{'设备名称':'设备名称','设备型号':'设备型号','设备区域':'设备区域'}]
shebeimingxi = {}
for i in range(1,nor):
    # print(table_0.row_values(i)[0])
    # shebeiliebiao.append(table_0.row_values(i))
    # shebeiliebiao[i]=shebeimingxi.setdefault('devname',table_0.row_values(i)[0],'dvexinghao',table_0.row_values(i)[1],'devquyu':table_0.row_values(i)[2])
    shebeimingxi={'设备名称':table_0.row_values(i)[0],'设备型号':table_0.row_values(i)[1],'设备区域':table_0.row_values(i)[2]}
    shebeiliebiao.append(shebeimingxi)
# print(len(shebeiliebiao))

####sql语句创建数据库或使用数据库，创建表格
sql_biaoge_shebeiliebiao = 'CREATE TABLE IF NOT EXISTS users (
    设备名称 varchar(255) PRIMARY KEY ,  
    设备型号 varchar(255) NOT NULL,                    
    设备区域 varchar(255) NOT NULL,                           
    备注 TEXT                             
)'

    











cursor.close()

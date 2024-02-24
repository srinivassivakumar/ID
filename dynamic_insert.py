import pandas as pd
import pymysql

tableName = input("Please enter the table name: ")
sheet_name = input("Please enter the excel sheet file name: ")
df = pd.read_excel(sheet_name + '.xlsx')

records = df.to_records(index = False)

columns_list = df.columns
my_string = []
for i in range(len(columns_list)):
    my_string.append('%s')

con = pymysql.connect(
        host='localhost',
        user='root',
        password='sri123',
        # port=3306',
        db='python_video'
    )
cursor = con.cursor()

for rec in records:
    sql = "INSERT INTO "+tableName+" ("+','.join(columns_list)+") VALUES ("+','.join(my_string)+")"
    print(sql)
    cursor.execute(sql, tuple(rec))
    con.commit()
    print("The record = {} has been uploaded successfully".format(rec))

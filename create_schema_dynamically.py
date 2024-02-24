import pandas as pd
import pymysql

tableName = input("Please enter the table name: ")
sheet_name = input("Please enter the excel sheet file name: ")
pk = input("Please enter column name if you know PK: ")
pk_query = ''
if pk:
    pk_query = ', PRIMARY KEY ('+pk+')'



df = pd.read_excel(sheet_name + '.xlsx')
# df = df.fillna('None')
df.fillna('None',inplace=True)

records = df.to_records(index = False)

columns_list = df.columns
my_string = []
schema_def = ""
for i in range(len(columns_list)):
    my_string.append('%s')
    if i+1 == len(columns_list):
        schema_def += str(columns_list[i]) + ' VARCHAR(40)'
    else:
        schema_def += str(columns_list[i]) + ' VARCHAR(40), '


drop_schema = 'DROP TABLE IF EXISTS '+tableName+''
create_schema = 'CREATE TABLE '+tableName+'('+schema_def+pk_query+');'

print(create_schema)

con = pymysql.connect(
        host='localhost',
        user='root',
        password='sri123',
        # port=3306',
        db='python_video'
    )
cursor = con.cursor()

cursor.execute(drop_schema)
cursor.execute(create_schema)
#
for rec in records:
    sql = "INSERT INTO "+tableName+" ("+','.join(columns_list)+") VALUES ("+','.join(my_string)+")"
    print(sql)
    cursor.execute(sql, tuple(rec))
    con.commit()
    print("The record = {} has been uploaded successfully".format(rec))

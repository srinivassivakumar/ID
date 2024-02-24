import pandas as pd
import pymysql

df = pd.read_excel('arraye.xlsx')

records = df.to_records(index = False)
print(type(records))
con = pymysql.connect(
        host='localhost',
        user='root',
        password='sri123',
        # port=3306',
        db='python_video'
    )
cursor = con.cursor()

for rec in records:
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='sri123',
        # port=3306',
        db='python_video'
    )
    cursor = con.cursor()
    sql = "INSERT INTO users (id, name,password) VALUES (%s, %s,%s)"
    cursor.execute(sql, tuple(rec))
    con.commit()
    print("The record = {} has been uploaded successfully".format(rec))

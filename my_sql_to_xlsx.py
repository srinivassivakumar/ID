import pandas as pd
import pymysql

tableName = input("Please enter the table name")
result_xlsx = input("Please enter the name of file you want to save as xlsx")

con = pymysql.connect(
        host='localhost',
        user='root',
        password='sri123',
        # port=3306',
        db='python_video'
    )
cursor = con.cursor()

cursor.execute("select * from "+tableName+"")
df = pd.DataFrame(cursor.fetchall())
df.to_excel(""+result_xlsx+".xlsx")

con.commit()

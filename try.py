import cx_Oracle
print(cx_Oracle.__file__)

con = cx_Oracle.connect("SYSTEM/oracle@localhost:1521/orclcdb")
cursor = con.cursor()

cursor.execute("Select 100 from dual")

for row in cursor:
    print(row)
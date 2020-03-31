import cx_Oracle

con = cx_Oracle.connect('SYSTEM/oracle@localhost:1521/orclcdb')
cur = con.cursor()
res = cur.execute('select 100 from dual')
print(res.fetchall())
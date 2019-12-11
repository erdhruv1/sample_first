import cx_Oracle
print(cx_Oracle.__file__)

con = cx_Oracle.connect("SYSTEM/oracle@localhost:1521/orclcdb")
print(dir(con))
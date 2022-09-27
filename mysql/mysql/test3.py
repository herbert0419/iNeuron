import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Jaijai1@11" )
cursor = mydb.cursor()
cursor.execute("select employe_id , emp_mailid from sudhanshu.ineuron1")
l = []
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[0]))
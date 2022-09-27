import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Jaijai1@11" )
cursor = mydb.cursor()
s = "insert into sudhanshu.ineuron1 values(101 , 'sudhanshu kumar', 'sudhanshu@ineuron.ai' ,100 , 30)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)

mydb.commit()
cursor.execute("select * from sudhanshu.ineuron1 ")
for i in cursor.fetchall():
    print( i)

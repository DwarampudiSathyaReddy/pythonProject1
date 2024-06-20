import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="Sathya@1234",database="mydb")
mycurs=mydb.cursor()
#print(mycurs)
#mycurs.execute("create database mydb")
#mycurs.execute("show databases")
#mycurs.execute("create table users(name varchar(50),email varchar(50),password varchar(50))")
#print(mycurs)
result=mycurs.execute("select * from user")
sql="insert into users(name,email,password)values(%s,%s,%s)"
val=("sathya","sathya@gmail.com",12345)
mycurs.execute(sql,val)
print(mycurs)
mycurs.execute("show tables")
for db in mycurs:
    print(db)
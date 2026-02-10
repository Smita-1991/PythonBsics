import sqlite3

RollNo=3
name="Dhruv"
address="Pune"

conn= sqlite3.connect("student.db",isolation_level=None)
conn.execute('create table if not exists Students (RollNo int PRIMARY KEY, name text, address text) strict')
conn.execute('INSERT INTO Students VALUES(1,"John","Pune")')
conn.execute('INSERT INTO Students VALUES(2,"Smita","Pune")')
conn.execute('insert into Students values(?,?,?)',[RollNo,name,address])
print(conn.execute('select * from Students').fetchall())
print(conn.execute('select RollNo,name from Students').fetchall())

for row in conn.execute('select * from Students').fetchall():
    print(row)
    print("{}{}".format(row[1]," is my favorite student"))

print(conn.execute('select RollNo,name from Students GROUP BY RollNo').fetchall())

print(conn.execute('select * from Students where RollNo="1"').fetchall())


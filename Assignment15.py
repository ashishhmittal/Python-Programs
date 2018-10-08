import sqlite3


#Question 1
try:
    con=sqlite3.connect('students.db')
    print("Database created successfully")
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("Problem :",e)
finally:
    if con:
        con.close()


#Question 2

lst=[]
i=0
while(i<10):
    a=input("Enter name: ")
    b=int(input("Enter marks: "))
    if(b<0 or b>100):
        print("Invalid marks")
        i=i-1
    else:
        
        lst.append((a,b))
        i=i+1



#Question 3

try:
    con=sqlite3.connect('students.db')
    cursor=con.cursor()
    query="create table students(sname varchar(10),marks int(3))"
    query2="insert into students(sname,marks) values(?,?)"
    cursor.execute(query)
    cursor.executemany(query2,lst)
    print("Table created")
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("Problem :",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()



#Question 4


try:
    con=sqlite3.connect('students.db')
    cursor=con.cursor()
    query="select * from students where marks>80"
    cursor.execute(query)
    data=cursor.fetchall()
    print("Students whose marks are mroe than 80 are: ")
    for row in data:
        print('Student name : {}'.format(row[0]))
    con.commit()

except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("Problem :",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()




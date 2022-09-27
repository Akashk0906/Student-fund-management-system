
import sqlite3,os
print("Enter year.....")
year=int(input())
print("Enter your semester")
sem=int(input())
print("Enter your roll no.")
r=int(input())
print("Enter your name")
name=input()
print("Enter your amount")
amt=int(input())
fname=year+sem
def register():
    st=os.path.join(os.getcwd(),str(fname))
    conn  = sqlite3.connect(st)
    mycursor = conn.cursor()
    mycursor.execute("create table if not exists student(Roll integer primary key,Name text,Amount text)")
    print("created")
    sq="insert into student(Roll, Name, Amount)values(?,?,?)"
    values=[r,name,amt]
    mycursor.execute(sq,values)
    mycursor.execute("select * from student")
    mycursor.close()
    conn.close()
def show():
    st=os.path.join(os.getcwd(),str(fname))
    conn  = sqlite3.connect(st)
    mycursor = conn.cursor()
    for row in mycursor:
        print(row[0],"\t",row[1],"\t",row[2])
    mycursor.close()
    conn.close()
register()
show()
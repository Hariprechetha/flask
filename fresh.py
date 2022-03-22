from flask import Flask, request
import sqlite3
app=Flask(__name__)
@app.get('/')
def hi():
    return "good night"
@app.post('/h')
def hi1():
    con = sqlite3.Connection("C:/Users/trc/Desktop/refresh/new/Scripts/old.db")
    cur=con.cursor()
    data = request.get_json()
    Name=data["Name"]
    Rollno=data["Rollno"]
    Mark=data["Mark"]
    student=(Name,Rollno,Mark)
    cur.execute("create table if not exists student(name varchar(255),Rollno varchar(255),mark int)")
    cur.execute("insert into student values(?,?,?)",student)
    con.commit()
    con.close()
    print(data)
    return "data collected"
@app.patch('/pat/<inputmark>')
def patchmethod(inputmark):
    data = request.get_json()
    users = data
    if inputmark in users.values():
        users["mark"] = 99
        res = "Data updated"
        return res
    print(f"The data after creation is {users}")
    res = "Data created"
@app.delete("/del/<inputmark>")
def deletemethod(inputmark):
    data = request.get_json()
    users = data
    if inputmark in users.values():
        del users["Mark"]
        res = "Data deleted"
        return res
    res = "Data not found"
    return res


@app.patch("/upd/<rollno>")
def update(rollno):
    updates(rollno);
    data = request.get_json()
    updates(data);
    return("updated");
def updates(data):
    con = sqlite3.Connection("C:/Users/trc/Desktop/refresh/new/Scripts/old.db")
    query = f'update student set name = {data["Name"]} where rollno ="{data["rollno"]}"';
    cur = con.cursor();
    cur.execute(query);
    con.commit();

@app.delete("/delete/<rollno>")
def deletes(rollno):
    delete(rollno);
    return("deleted");
def delete(rollno):
    con = sqlite3.Connection("C:/Users/trc/Desktop/refresh/new/Scripts/old.db")
    query = f'delete from student where rollno = "{rollno}"';
    cur = con.cursor();
    cur.execute(query)
    con.commit()
app.run(debug=True)




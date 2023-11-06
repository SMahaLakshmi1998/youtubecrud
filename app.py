from flask import Flask,render_template,request,redirect,url_for
import sqlite3 as sql
app=Flask(__name__)

@app.route('/read')
def home():
    conn=sql.connect("youtube.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from clone")
    data=cur.fetchall()
    return render_template("sample.html",datas=data)



@app.route('/video<id>')
def video(id):
     conn=sql.connect("youtube.db")
     conn.row_factory=sql.Row
     cur=conn.cursor()
     cur.execute("select * from clone where id=?",(id,))
     data=cur.fetchone()
     
     return render_template("happy.html", datas=data)



if __name__=="__main__":
        app.run(debug=True)

from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)
var = ""

@app.route("/")
def home(): 
    
    return render_template("layout.html")

@app.route("/upload.html")
def upload():
    conn = sqlite3.connect("wallpapersite.db")
    cur = conn.cursor()
    data = cur.execute("SELECT tag FROM photos WHERE tag='d'")                                                                                                                                                               
    data = cur.fetchone()
    var = data
    print(data)
    return render_template("layout.html", var = var[0])


if __name__ == "__main__": 
    app.run(debug=True)
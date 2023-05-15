from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template("layout.html")

@app.route("/upload.html")
def upload():
    conn = sqlite3.connect("wallpapersite.db")
    cur = conn.cursor()
    data = cur.execute("SELECT tag FROM photos WHERE tag='d'")                                                                                                                                                               
    data = cur.fetchall()
    return render_template("upload.html")

if __name__ == "__main__": 
    app.run(debug=True)
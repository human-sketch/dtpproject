from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)
@app.route("/") 
def home():                                                                                               
    return render_template("layout.html")


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    conn = sqlite3.connect("wallpapers.db")
    cur = conn.cursor()
    tag = request.form['name_v']
    data = cur.execute("INSERT INTO photos ('tag') VALUES (?)", (tag,))
    cur.connection.commit()   
    print(tag)                                                                                                                                                            
    return render_template("layout.html")

@app.route("/contact")
def contact(): 
    return render_template("contact.html")


@app.route("/fileupload", methods=['GET', 'POST'])
def fileupload(): 
    if request.method == 'POST': 
        conn = sqlite3.connect("wallpapers.db")
        cur = conn.cursor()
        tag = request.form['tag']
        file = request.files['filename']
        

        data = cur.execute("INSERT INTO photos ('tag', 'image') VALUES (?, ?)", (tag,file))
        cur.connection.commit()   
    return render_template("fileupload.html")



if __name__ == "__main__": 
    app.run(debug=True)



from flask import Flask, render_template 
import sqlite3
from pathlib import Path

app = Flask(__name__, template_folder='templates') 
base_path = Path(__file__).resolve().parent  # Getting the parent directory of the current script
db_folder = base_path.parent / 'database'  # Assuming the database folder is at the parent level

# Specify the database file path relative to the current script
db_name = "immigration.db"
file_path = db_folder / db_name

@app.route("/") 
def index(): 
    return render_template("home-page.html") 

@app.route("/about") 
def about(): 
    return render_template("about.html") 

@app.route("/data") 
def data():
    con = sqlite3.connect(file_path)
    cursor = con.cursor()
    canada = cursor.execute("select * from canada limit 10").fetchall()
    con.close()
    return render_template("data.html", canada=canada)

if __name__ == "__main__":
    app.run(debug=True)

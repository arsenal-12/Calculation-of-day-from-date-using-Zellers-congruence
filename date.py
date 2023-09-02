from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    
    k = year % 100
    j = year // 100
    
    day_of_week = (day + 13*(month+1) // 5 + k + k//4 + j//4 + 5*j) % 7
    
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    return days[day_of_week]

@app.route("/")
def index():
    return render_template("date.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    day = int(request.form["day"])
    month = int(request.form["month"])
    year = int(request.form["year"])

    day_name = zellers_congruence(day, month, year)
    return render_template("date.html", day_name=day_name, day=day, month=month, year=year)

if __name__ == "__main__":
    app.run(debug=True)

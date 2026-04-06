from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

FILE = "expenses.csv"

@app.route("/")
def index():
    expenses = []
    try:
        with open(FILE, newline='') as f:
            reader = csv.reader(f)
            expenses = list(reader)
    except:
        pass
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    amount = request.form["amount"]

    with open(FILE, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, amount])

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
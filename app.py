from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)

database.init_db()

@app.route("/")
def home():
    tasks = database.get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if title:
        database.add_task(title)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

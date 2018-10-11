from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/M&G/Desktop/Python Dünyası/PythonWeb/TodoApp/gokalptodo.db'
db = SQLAlchemy(app)

# ANASAYFA
@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html",todos=todos)

# Todo Ekleme
@app.route("/add",methods=["POST"])
def addTodo():
    title = request.form.get("title")
    newTodo = Todo(title=title,isComplete=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

# Todo Güncelleme
@app.route("/edit/<string:id>")
def editTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.isComplete = not todo.isComplete
    db.session.commit()
    return redirect(url_for("index"))

# Todo Silme
@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

# Todo Veritabanı Tablosu
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    isComplete = db.Column(db.Boolean)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
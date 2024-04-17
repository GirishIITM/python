from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='template')

todos = []


@app.route("/", )
def index():
    return render_template('todo.html', todos=todos)


@app.route("/add", methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    todos.append(todo)
    return redirect(url_for('todo'))


@app.route("/delete/<int:todo_index>", methods=["DELETE"])
def delete_todo(todo_index):
    del todos[todo_index]
    return redirect(url_for("todo"))


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

todos = [
    {   
        "id": 1,
        "task": "Exercise",
        "done": False
    },
    {
        "id": 2,
        "task": "Learn Flask",
        "done": False
    },
    {
        "id": 3,
        "task": "Poop",
        "done": True
    }
]

@app.route("/")
def todos_index():
    return render_template("todos.html", todos=todos)

@app.route("/todo/<int:id>", methods=["PUT"])
def update_todo(id: int):
    for todo in todos:
        if todo["id"] == id:
            todo["done"] = not todo["done"]

    return render_template("todos.html", todos=todos)

@app.route("/create_todo", methods=["POST"])
def create_todo():
    todos.append({
        "id": len(todos) + 1,
        "task": request.form["task"],
        "done": False
    })

    return render_template("todos.html", todos=todos)

@app.route('/delete_completed', methods=['DELETE'])
def delete_completed():
    for i, todo in enumerate(todos):
        if todo["done"]:
            todos.pop(i)
    return render_template("todos.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True)
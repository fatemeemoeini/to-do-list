from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return "Welcome to the To-Do List API."

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task_id = len(tasks)+ 1
    task = {
        'id': task_id,
        'title': data.get('title'),
        'description': data.get('description')
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify(task), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    return jsonify(task), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)

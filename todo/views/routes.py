from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route('/health', methods=['GET'])
def health():
    json = jsonify({"status": "ok"})
    status_code = 200
    return json, status_code

@api.route('/todos', methods=['GET'])
def get_todos():
    json = jsonify([{
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": False,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
        }])
    status_code = 200
    return json, status_code

@api.route('/health', methods=['GET'])
def get_todo(id):
    json = jsonify([{
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": False,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
        }]), 200
    status_code = 200
    return json, status_code

@api.route('/todos', methods=['POST'])
def create_todo():
    json = jsonify({
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
        }), 201
    status_code = 201
    return json, status_code

@api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    json = jsonify({
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
        }), 200
    status_code = 200
    return json, status_code

@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    json = jsonify({
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
        }), 200
    status_code = 200
    return json, status_code
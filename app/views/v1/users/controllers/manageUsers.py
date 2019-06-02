from flask.globals import request
from flask.json import jsonify
from flask_restful import reqparse

from app.models import Users
from app.repository import BaseResources
from app.views.v1.users import v1_users


@v1_users.route('', methods=['GET', 'POST'])
@v1_users.route('/<id>', methods=['GET', 'PUT', 'DELETE'])
def manageUsers(id=None):

    if request.method == 'GET':
        result = BaseResources(Users).getAll()
        return jsonify(result['response']), result['status']
        
    
    if request.method == 'POST':
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('birthday', required=True)
        parser.add_argument('password', required=True)
        data = parser.parse_args()
    
        result = BaseResources(Users).postData(data)
        return jsonify(result['response']), result['status']

    if request.method == 'PUT':
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('birthday', required=True)
        parser.add_argument('password', required=True)
        parser.add_argument('status', required=True)
        data = parser.parse_args()

        result = BaseResources(Users).putData({'id':id}, data)
        return jsonify(result['response']), result['status']
    
    if request.method == 'DELETE':
        result = BaseResources(Users).deleteData({'id':id})
        return jsonify(result['response']), result['status']

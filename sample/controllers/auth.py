from flask_restful import Resource
from ..models import user
from ..utils import *

class Login(Resource):
    def get(self):
        user.User.add_user('John')
        return responses.error('This tests that utils works.')

from . import api
import controllers

def add_routes():
    api.add_resource(controllers.auth.Login, '/')

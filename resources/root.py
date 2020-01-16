from flask_restful import Resource, Api

class Root(Resource):
    def get(self):
        return {"Welcome!":"Ollivanders"}
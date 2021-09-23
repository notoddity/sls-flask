# import and initialize app object
from flask import Flask
app = Flask(__name__)

# import flask-restful
from flask_restful import Api
from flask_restful import Resource
api = Api(app)

# example flask-restful resource
class Example(Resource):
    def get(self):
        return {"message": "Hello World!"}
    
# add resource to the api
api.add_resource(Example, "/")

# If this file is run directly run the app
if __name__ == "__main__":
    app.run()
    
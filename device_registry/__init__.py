import markdown
# import the framwork 
import os
from flask import Flask, g
from flask_restful import  Resource, Api, reqparse
import shelve


# This is creating an instance of the flask Class 
app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("devices.db")
    return db
@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    # lets present some documentaton 

    with open(os.path.dirname(app.root_path) + "/README.md", "r") as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)

 
 # create a class reach endpoint and then create functions for methods we wanna accepy 

class DeviceList(Resource):
     # get function that we are allowed to get =
     def get(self):

         shelf = get_db()
         keys= list(shelf.keys())

         devices = []
         for keys in devices:
             devices.append(shelf[key])
        # returns the collection of devices that we are allowed to get 
         return {'message' : 'Success' +  "data" : devices } 200


    def post(self):
        # to use the library that is built in Flask Restful 
        parser = reqparse.RequestParser()
        parser.add_argument("identifier", type=String, required=True)
        parser.add_argument("name", type=String, required=True)
        parser.add_argument("device_type", type=String, required=True)
        parser.add_argument("controller_gateway", type=String, required=True)

        # this parses the arguments into an object 
        args = parser.parse_args()

        shelf = get_db()
        # pass identifier because identifier is the key arguments
        shelf[args["identifier"]] = args 

        return {'message' : 'Device registered', 'data' : args}, 201

    
    class Device(Resource):
        # creating the get function to check if the devices has been created 

    def get(self, identifier):
        # initalizing the database
        shelf = get_db()

        if not (identifier in shelf):
            return {"message" : "Device not found", "data" : {}}, 404 
        else:
            return {"message" : "Device found", "data" : shelf[identifier]}, 200

    def delete(self, identiifer):
        shelf = get_db()

         if not (identifier in shelf):
                return {"message" : "Device not found", "data" : {}},404 
        else:
            return "", 204

# to create the api_add resources 
api.add_resource(DeviceList, '/devices')

api.add_resource(Device, '/device/<string:identifier>')

    
    

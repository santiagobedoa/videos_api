# REST API for Video Streaming Platform

## Description
we're going to build a RESTful API in Python using the module **Flask**. Flask it's really known for making micro web services because it's a very lightweight module. For anyone's unfamiliar with the term REST or API I'll quickly define them for you.

### REST & API
* Stands for REpresentational State Transfer.
* Stands for Application Programming Interface.

Essentially, what a REST API is, is a way for other programs or applications to make CRUD (create, read, update, delete) operations. It's a way to deal with some kind of data in a structured format. We set up an API that has a bunch of endpoints.

### Endpoints
Endpoints are essentially almost like commands or you can think of them almost as just requests. An endpoint send a request and will return a response based on the request that was given. For example, if the request was give me all of the views that are on a specific video, the response would be the number of views that were on that video, let's say that the video didn't exist then the response would be something like 404 not found.

# Flask Quickstart
A minimal Flask application looks something like this:
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
So what did that code do?
* First we imported the Flask class. An instance of this class will be our WSGI application.
* Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
* We then use the route() decorator to tell Flask what URL should trigger our function.
* The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

Save it as hello.py or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.
To run the application, use the flask command or python -m flask. You need to tell the Flask where your application is with the --app option.
```
flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 ```

 ## flask-restfull
 A minimal Flask-RESTful API looks like this:
 ```
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# endpoint definition
class HelloWorld(Resource):
    # what will be executed when get method is requested
    def get(self):
	# make sure that the object returned is serializable and deserializable
      	return {'hello': 'world'}

# adding the endpoint and the class that contains the actions
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```

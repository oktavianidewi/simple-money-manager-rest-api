# proses import library flask, sehingga code flask bisa diakses di aplikasi.
import flask

# Creates the Flask application object, which contains data about the application and also methods (object functions) that tell the application to do certain actions.
app = flask.Flask(__name__)

# Starts the debugger. With this line, if your code is malformed, you’ll see an error when you visit your app. Otherwise you’ll only see a generic message such as Bad Gateway in the browser when there’s a problem with your code.
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello world!</h1>"

# Starts the debugger. With this line, if your code is malformed, you’ll see an error when you visit your app. Otherwise you’ll only see a generic message such as Bad Gateway in the browser when there’s a problem with your code.
app.run()
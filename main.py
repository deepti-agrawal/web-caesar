from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/submit" method="POST">
            Rotate by: <input type="text" name="rot" value="0">
            <textarea rows="4" cols="50" name="text"></textarea>
            <input type="submit" value="Submit Query">
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/submit",methods = ['POST'])
def encrypt():
    rot = int(request.form['rot'])
    message = request.form['text']
    encrypted_message = rotate_string(message,rot)
    return "<H1> Encrypted message is: "+encrypted_message+"</H1>"

app.run()
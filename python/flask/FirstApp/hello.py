from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World - from a file that isn't app.py 2222222!"


"""
To be able to run this file using Flask from VSCode I needed to modify launch.json.
Changed the Python: Flask entry to the following:
    * Changed "FLASK_APP": "app.py" line to "FLASK_APP": "${file}"
    * Without the modification it was always expecting the app.py file to be in project root directory
        * Not sure how it is determining this project root directory yet!
    * File modified /Users/kershaw1/vue/real-world-vue/.vscode/launch.json

Here's what I changed to:

{
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "${file}"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true
}, 
"""
from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello World from docker container from pipeline pollSCM branch new!"
if __name__ == "__main__":
    app.run('0.0.0.0')

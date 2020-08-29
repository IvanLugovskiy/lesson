from flask import Flask

app = Flask(__name__)


@app.route('/home/')
def requirements():
    v = open("requirements.txt")
    data = v.read()
    return data

if __name__ == "__main__":
    app.run()



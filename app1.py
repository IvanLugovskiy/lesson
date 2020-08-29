from flask import Flask
from faker import Faker

app1 = Flask(__name__)


@app1.route('/home/')
def generate():
    f = Faker()
    data = ''
    for _ in range(100):
        data += f.email() + f.name()
    return data
    print('\n'.join(data))

if __name__ == "__main__":
    app1.run()



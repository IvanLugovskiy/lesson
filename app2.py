from flask import Flask
from faker import Faker
from utils import exec_query

app1 = Flask(__name__)


@app1.route('/home/')
def generate():
    f = Faker()
    data = ''
    for _ in range(100):
        data += f.email() + f.name()
    return data
    print('\n'.join(data))

@app1.route('/test/')
def foo():
    return str(exec_query('SELECT * FROM customers;'))

if __name__ == "__main__":
    app1.run()

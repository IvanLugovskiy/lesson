from flask import Flask
from faker import Faker
from utils import exec_query

app1 = Flask(__name__)

@app1.route('/test/')
def foo():
    return str(exec_query('SELECT * FROM customers;'))

if __name__ == "__main__":
    app1.run()

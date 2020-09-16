from flask import Flask
from faker import Faker
from utils import exec_query
#import pdb; pdb.set_trace()
import requests
import sqlite3

app1 = Flask(__name__)


@app1.route('/names/')
def names():
    import sqlite3
    conn = sqlite3.connect('./chinook.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT (DISTINCT FirstName) FROM customers;')
    res = cursor.fetchall()
    conn.close()
    return str(res)




#    return str(exec_query('SELECT * FROM customers;'))

if __name__ == "__main__":
    app1.run()


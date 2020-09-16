from flask import Flask
from faker import Faker
from utils import exec_query
#import pdb; pdb.set_trace()
import requests
import sqlite3

app3 = Flask(__name__)


@app3.route('/tracks-sec/')
def names():
    import sqlite3
    conn = sqlite3.connect('./chinook.db')
    cursor = conn.cursor()
    cursor.execute('SELECT (Name), (Milliseconds) FROM tracks;')
    res = cursor.fetchall()
    conn.close()
    return str(res)



if __name__ == "__main__":
    app3.run()


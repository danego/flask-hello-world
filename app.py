from flask import Flask
import psycopg2

app = Flask(__name__)


db_url = postgresql://lab10_7v8p_user:EcXQ0yqF6OonTspFvrKkrSvhUFzqLH6Q@dpg-dbp5n5h42hec73blj7rg-a/lab10_7v8p

@app.route('/')
def hello_world():
    return "Hello World from Dane in 3308"

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect(db_url)
    conn.close()
    return "Database connection successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect(db_url)

    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    
    conn.close()
    return "Basketball table successfully created"
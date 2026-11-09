from flask import Flask
import psycopg2

app = Flask(__name__)


# postgresql://lab10_7v8p_user:EcXQ0yqF6OonTspFvrKkrSvhUFzqLH6Q@dpg-dbp5n5h42hec73blj7rg-a/lab10_7v8p

@app.route('/')
def hello_world():
    return "Hello World from Dane in 3308"

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab10_7v8p_user:EcXQ0yqF6OonTspFvrKkrSvhUFzqLH6Q@dpg-dbp5n5h42hec73blj7rg-a/lab10_7v8p")

    conn.close()
    return "Database connection successful"
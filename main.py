import sqlite3
import pandas as pd
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    post = cur.execute('SELECT * FROM dbdataframe').fetchall()
    posts = json.dumps(post)
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':

        conn = sqlite3.connect('database.db')
        delete_task(conn)
        list = request.form.getlist('veri')
        new_list = list[0]
        list_dict = json.loads(new_list)
        print(list_dict)

        i = 0
        while i != len(list_dict):
            row = list_dict[i]
            keys = []
            values = []
            for key, value in row.items():
                keys.append(key)
                values.append(value)
            i += 1
            print(values)
            update_task(conn, values)

    return " "


def update_task(conn, task):
    sql = """ """ #sqlcommand
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def delete_task(conn):
    sql = """ """#sqlcommand
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


if __name__ == '__main__':
    app.run(debug=True)

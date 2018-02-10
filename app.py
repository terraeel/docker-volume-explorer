import sqlite3
import json
from flask import Flask, request

app = Flask(__name__)


def get_volumes():
    with sqlite3.connect('volumes.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM volumes ORDER BY name")
        all_volumes = cursor.fetchall()
        return all_volumes


@app.route('/api/volumes', methods=['GET'])
def collection():
    volumes = get_volumes()
    return json.dumps(volumes)

if __name__ == '__main__':
    app.debug = True
    app.run()

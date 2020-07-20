import os
import datetime
# import sys
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# print(app.config, file=sys.stderr)
# to see the config in logs
# docker-compose -f docker-compose-dev.yml logs

# instantiate the db
db = SQLAlchemy(app)



@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
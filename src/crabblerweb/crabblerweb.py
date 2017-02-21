# coding: utf-8
# as per http://www.python.org/dev/peps/pep-0263/

import json
import uuid
from datetime import datetime

from flask import Flask, jsonify, make_response, Markup, request, url_for
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['threaded'] = True
app.config['ip_address'] = '0.0.0.0'

import logging
from logging.handlers import RotatingFileHandler

log_pathname = 'var/crabbler_web.log'
file_handler = RotatingFileHandler(log_pathname, maxBytes=1024* 1024 * 10 , backupCount=1024)
file_handler.setLevel( app.config['DEBUG'] )
formatter = logging.Formatter("%(levelname)s | %(asctime)s |  %(module)s | %(funcName)s | %(message)s")
file_handler.setFormatter(formatter)
app.logger.setLevel('DEBUG')
app.logger.addHandler(file_handler)

def now():
    return str(datetime.now().strftime('%Y-%m-%dT%H-%M-%S'))

@app.route("/")
def root():
    this_route = url_for('.root')
    msg = "Hello Crab Fans"
    statuscode = 200
    app.logger.info(json.dumps(msg))
    if 'text/html' in request.headers.get("Accept", ""):
        return Markup(msg), statuscode
    else:
        return jsonify( {'status':'ko', 'statuscode':statuscode, 'message':msg} ), statuscode

@app.route("/api/0.1/auth", methods=['POST'])
def legacy_api_auth():
    msg = "Legacy auth API"
    status = "ok"
    statuscode = 200
    app.logger.info(json.dumps(msg))

    dt = now()
    t = str(uuid.uuid4())
    json_data = request.json

    json_data['token'] = t 
    app.logger.info(json.dumps(json_data))
    

    filename = dt + "_" + t + ".json"
    pathname = 'data/auth/'+filename

    with open(pathname, 'w') as outfile:
        json.dump(json_data, outfile)

    return jsonify( {'status':status, 'statuscode':statuscode, 'access_token':t} ), statuscode


@app.route("/api/0.2/users", methods=['POST'])
def legacy_api_users():
    msg = "Legacy users API"
    status = "ok"
    statuscode = 200
    app.logger.info(json.dumps(msg))

    dt = now()
    u = str(uuid.uuid4())
    json_data = request.json
    json_data['uuid'] = u

    app.logger.info(json.dumps(json_data))
    
    
    filename = dt + "_" + u + ".json"
    pathname = 'data/users/'+filename

    with open(pathname, 'w') as outfile:
        json.dump(json_data, outfile)

        
    return jsonify( {'status':status, 'statuscode':statuscode, 'phone_id':u} ), statuscode


@app.route("/api/0.2/sightings", methods=['POST', 'GET'])
@app.route("/up", methods=['POST', 'GET'])
def up():
    if request.method == 'POST':
        json_data = request.json
        app.logger.info(json.dumps(json_data))
    
        dt = now()
        u = str(uuid.uuid4())
        filename = dt + "_" + u + ".json"
        pathname = 'data/sightings/'+filename
        
        with open(pathname, 'w') as outfile:
            json.dump(json_data, outfile)


        msg = "Sightings uploaded successfully."
        statuscode = 200
        app.logger.info(json.dumps(msg))
        if 'text/html' in request.headers.get("Accept", ""):
            return Markup(msg), statuscode
        else:
            return jsonify( {'status':'ok', 'statuscode':statuscode, 'message':msg} ), statuscode


    else:
        statuscode = 200
        if 'text/html' in request.headers.get("Accept", ""):
            page='''
            <html>
            <body>
            <b>Nothing to see here ;)</b>
            </body>
            </html>
            '''
            return Markup(page), statuscode
        else:
            msg = "Nothing to see here ;)"
            return jsonify( {'status':'ok', 'statuscode':statuscode, 'message':msg} ), statuscode


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


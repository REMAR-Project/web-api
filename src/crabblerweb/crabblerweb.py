# coding: utf-8
# as per http://www.python.org/dev/peps/pep-0263/

import json
import logging
import uuid
import datetime

from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, Markup, request, url_for
app = Flask(__name__)


def logs(app):
    log_pathname = 'var/crabbler_web.log'
    file_handler = RotatingFileHandler(log_pathname, maxBytes=1024* 1024 * 10 , backupCount=1024)
    file_handler.setLevel( app.config['DEBUG'] )
    formatter = logging.Formatter("%(levelname)s | %(asctime)s |  %(module)s | %(funcName)s | %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel('DEBUG')
    app.logger.addHandler(file_handler)

@app.errorhandler(400)
def error_400(e):
    statuscode = 400
    msg = {"Method": request.method, "URL":request.url}
    app.logger.error(json.dumps(msg))
    if 'text/html' in request.headers.get("Accept", ""):
        return Markup(str(statuscode)+" "+msg), statuscode
    else:
        return jsonify( {'status':'ko', 'statuscode': statuscode, 'message':msg} ), statuscode

@app.errorhandler(401)
def error_401(e):
    statuscode = 401
    msg = {"Method": request.method, "URL":request.url}
    app.logger.error(json.dumps(msg))
    if 'text/html' in request.headers.get("Accept", ""):
        return Markup(str(statuscode)+" "+msg), statuscode
    else:
        return jsonify( {'status':'ko', 'statuscode': statuscode, 'message':msg} ), statuscode

@app.errorhandler(403)
def error_403(e):
    statuscode = 403
    msg = {"Method": request.method, "URL":request.url}
    app.logger.error(json.dumps(msg))
    if 'text/html' in request.headers.get("Accept", ""):
        return Markup(str(statuscode)+" "+msg), statuscode
    else:
        return jsonify( {'status':'ko', 'statuscode': statuscode, 'message':msg} ), statuscode

@app.errorhandler(404)
def error_404(e):
    statuscode = 404
    msg = {"Method": request.method, "URL":request.url}
    app.logger.error(json.dumps(msg))
    if 'text/html' in request.headers.get("Accept", ""):
        return Markup(str(statuscode)+" "+msg), statuscode
    else:
        return jsonify( {'status':'ko', 'statuscode': statuscode, 'message':msg} ), statuscode

@app.errorhandler(405)
def error_405(e):
    statuscode = 405
    msg = {"Method": request.method, "URL":request.url}
    app.logger.error(json.dumps(msg))
    if 'text/html' in request.headers.get("Accept", ""):
        return Markup(str(statuscode)+" "+msg), statuscode
    else:
        return jsonify( {'status':'ko', 'statuscode': statuscode, 'message':msg} ), statuscode

@app.errorhandler(410)
def error_410(e):
    statuscode = 410
    msg = {"Method": request.method, "URL":request.url}
    app.logger.error(json.dumps(msg))
    if 'text/html' in request.headers.get("Accept", ""):
        return Markup(str(statuscode)+" "+msg), statuscode
    else:
        return jsonify( {'status':'ko', 'statuscode': statuscode, 'message':msg} ), statuscode

@app.errorhandler(500)
def error_500(e):
    statuscode = 500
    msg = {"Method": request.method, "URL":request.url}
    app.logger.error(json.dumps(msg))
    if 'text/html' in request.headers.get("Accept", ""):
        return Markup(str(statuscode)+" "+msg), statuscode
    else:
        return jsonify( {'status':'ko', 'statuscode':statuscode, 'message':msg} ), statuscode

@app.route("/")
def root():
    this_route = url_for('.root')
    app.logger.info("Logging a test message from "+this_route)
    msg = "Hello Crab Fans"
    statuscode = 200
    app.logger.info(json.dumps(msg))
    if 'text/html' in request.headers.get("Accept", ""):
        return Markup(msg), statuscode
    else:
        return jsonify( {'status':'ko', 'statuscode':statuscode, 'message':msg} ), statuscode

@app.route("/up", methods=['POST', 'GET'])
def up():
    if request.method == 'POST':
        json_data = request.json
    
        dt = str(datetime.datetime.now().isoformat())
        u = str(uuid.uuid4())
        filename = dt + "_" + u + ".json"
        pathname = 'data/'+filename
        
        with open(pathname, 'w') as outfile:
            json.dump(json_data, outfile)

        msg = "File Uploaded to " + pathname
        statuscode = 200
        app.logger.info(json.dumps(msg))
        if 'text/html' in request.headers.get("Accept", ""):
            return Markup(msg), statuscode
        else:
            return jsonify( {'status':'ko', 'statuscode':statuscode, 'message':msg} ), statuscode


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
    logs(app)
    app.run(host="0.0.0.0", debug=True)


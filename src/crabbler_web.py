import json
import logging
import uuid
import datetime

from logging.handlers import RotatingFileHandler
from flask import Flask, request, url_for
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
def status_404(exception):
    msg = {"Method": request.method, "URL":request.url}
    app.logger.error(json.dumps(msg))
    app.logger.exception(exception)
    return "400", 400

@app.route("/")
def root():
    this_route = url_for('.root')
    app.logger.info("Logging a test message from "+this_route)
    return "Hello Crabs! "

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

        return "File Uploaded to " + pathname, 200

    else:
        page='''
        <html>
        <body>
        <b>Nothing to see here ;)</b>
        </body>
        </html>
        '''
        return page, 200


if __name__ == "__main__":
    logs(app)
    app.run(host="0.0.0.0", debug=True)


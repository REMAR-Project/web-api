import logging

from logging.handlers import RotatingFileHandler
from flask import Flask, url_for
app = Flask(__name__)

def logs(app):
    log_pathname = 'var/crabbler_web.log'
    file_handler = RotatingFileHandler(log_pathname, maxBytes=1024* 1024 * 10 , backupCount=1024)
    file_handler.setLevel( app.config['DEBUG'] )
    formatter = logging.Formatter("%(levelname)s | %(asctime)s |  %(module)s | %(funcName)s | %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel('DEBUG')
    app.logger.addHandler(file_handler)

@app.route("/")
def root():
    this_route = url_for('.root')
    app.logger.info("Logging a test message from "+this_route)
    return "Hello Crabs!"


if __name__ == "__main__":
    logs(app)
    app.run(host="0.0.0.0", debug=True)


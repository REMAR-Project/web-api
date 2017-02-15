# coding: utf-8
# as per http://www.python.org/dev/peps/pep-0263/

import logging

from logging.handlers import RotatingFileHandler

def init(app):
    app.config['DEBUG'] = True
    app.config['threaded'] = True
    app.config['ip_address'] = '0.0.0.0'

def logs(app):
    log_pathname = 'var/crabbler_web.log'
    file_handler = RotatingFileHandler(log_pathname, maxBytes=1024* 1024 * 10 , backupCount=1024)
    file_handler.setLevel( app.config['DEBUG'] )
    formatter = logging.Formatter("%(levelname)s | %(asctime)s |  %(module)s | %(funcName)s | %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel('DEBUG')
    app.logger.addHandler(file_handler)

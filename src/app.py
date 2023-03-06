# Simple flask app to test logging

from flask import Flask, request, render_template
from utils.logging.custom_logging import logger,ch
import logging
import os
os.environ["WERKZEUG_RUN_MAIN"] = "true"  # removes message 'started serving APP'


def setup_loging():

    """Remove werkzeug logging handler and add custom logging handler"""
    flask_logger = logging.getLogger('werkzeug')  # grabs underlying WSGI logger
    for _handler in flask_logger.handlers:
        flask_logger.removeHandler(_handler)
    flask_logger.name = logger.name
    flask_logger.addHandler(ch)


setup_loging()

logger.debug('Starting Flask APP')
app = Flask(__name__)
app.logger.disabled = True


@app.route("/")
def home():
    logger.debug('Checking DEBUG message')
    logger.info('Checking INFO message')
    logger.warning('Checking WARNING message')
    logger.critical('Checking CRITICAL message')
    logger.error('Checking ERROR message')
    return "Hello World!"


# handling CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


if __name__ == "__main__":
    app.run(debug=True)

# Simple flask app to test log_utils
import logging
import os
from flask import Flask
from utils.log_utils.custom_logging import CustomLogging
from common import add
#CustomLogging().set_appname_loglevel()

logger = CustomLogging().app_logger()

os.environ["WERKZEUG_RUN_MAIN"] = "true"  # removes message 'started serving APP'

def setup_loging():

    """Remove werkzeug log_utils handler and add custom log_utils handler"""
    flask_logger = logging.getLogger('werkzeug')  # grabs underlying WSGI logger
    for _handler in flask_logger.handlers:
        flask_logger.removeHandler(_handler)
    flask_logger.name = logger.name
    flask_logger.addHandler(CustomLogging.ch)


setup_loging()

logger.debug('Starting Flask APP')
app = Flask(__name__)
app.logger.disabled = True


@app.route("/")
def home():
    add(1,2)
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
    app.run(debug=False)

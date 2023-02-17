# Simple flask app to test logging

from flask import Flask, request, render_template
from utils.logging.custom_logging import logger


logger.debug('Starting Flask APP')
app = Flask(__name__)


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

import os
import logging
from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

GLITCHTIP_DSN = os.environ['DSN']

sentry_sdk.init(
    dsn=GLITCHTIP_DSN,
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)
app.config['DEBUG'] = False

@app.before_first_request
def setup_logging():
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    app.logger.info('logs enabled')

@app.route('/')
def root():
    return 'hello, world'

@app.route('/log-error')
def log_error():
    app.logger.error('logging error with glitchtip')
    return 'logged error'

@app.route('/trigger-error')
def trigger_error():
    division_by_zero = 1 / 0

if __name__ == '__main__':
    app.logger.info('starting server')
    app.run()

import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = False

@app.before_first_request
def setup_logging():
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

@app.route('/', methods=['POST'])
def webhook():
    payload = request.get_json(force=True)
    app.logger.info(payload)
    return jsonify(payload)

@app.route('/health', methods=['GET'])
def health():
    payload = {'status': 'up'}
    return jsonify(payload)

if __name__ == '__main__':
    app.logger.info('starting server')
    app.run()

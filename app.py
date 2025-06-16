from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    user = data.get('username')
    pwd  = data.get('password')
    if user == 'admin' and pwd == 'secret':
        logging.info(f"SUCCESS login for {user}")
        return {'status':'success'}, 200
    else:
        logging.warning(f"FAILED login for {user}")
        return {'status':'fail'}, 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

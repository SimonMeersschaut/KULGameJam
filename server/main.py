from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/post_score', methods=['POST'])
def post_score():
    try:
        data = request.get_json()
    except:
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
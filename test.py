from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, ice!'

@app.route('/kuma')
def hello_kuma():
    return 'Hello, kuma!'

if __name__ == "__main__":
    app.run(debug=True)
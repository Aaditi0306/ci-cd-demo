from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Service A works!</h1><h1>Service B works!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)


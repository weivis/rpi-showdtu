from flask import Flask, request
app = Flask(__name__)

@app.route('/iot')
def hello_world():
    data = request.args.get("data")
    print("data:",data)
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
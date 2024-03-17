from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return 'Ola !'

if __name__ == '__main__':
    app.run(debug=True)






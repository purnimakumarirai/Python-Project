from flask import Flask
app = Flask(__name__)
@app.route('/')
def flask_world():
    return 'This is flask application'
if __name__ == '__main__':
    app.run()

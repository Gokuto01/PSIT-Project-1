from flask import Flask, jsonify
from flask_cors import CORS
from route import get_all, get_name, get_genres

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/')

@app.route('/get_all')
def return_all():
    return jsonify(get_all())

@app.route('/get_name/<name>')
def return_name(name):
    return jsonify(get_name(name))

@app.route('/get_genres/<genres>')
def return_genres(genres):
    return jsonify(get_genres(genres))

if __name__ == '__main__':
    app.run(debug=True)

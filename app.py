from Flask import Flask, jsonify
from Flask_cors import CORS
from route import get_all, get_genres, get_name
from data_base import anime_data

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/')

@app.route('/get_all')
def return_all():
    return jsonify(get_all())

@app.route('/get_name/<name>')
def return_anime(name):
    return jsonify(get_anime(name))
    
@app.route('/get_genres/<genres>')
def return_genres(genres):
    return jsonify(get_genres(gen))
    

if __name__ == '__main__':
    app.run(debug=True)

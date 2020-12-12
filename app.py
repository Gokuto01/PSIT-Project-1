from Flask import Flask, render_template, jsonify, request
from Flask_cors import CORS
from route import get_all, get_genres, get_name
from data_base import anime_list

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/')

@app.route('/get_all')
def return_all():
    return jsonify(get_all())

@app.route('/get_name/<name>')
def return_anime(name):
    return jsonify(get_anime(name))
    
@app.route('/get_gen/<type>')
def return_gen(gen):
    return jsonify(get_genres(gen))
    

if __name__ == '__main__':
    app.run(debug=True)

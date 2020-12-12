from Flask import Flask, render_template, jsonify, request
from Flask_cors import CORS
from route import get_name, link_anime, select_type
from data_base import anime_list

name_link = anime_dict()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/')
def home():
    return jsonify(data)

@app.route('/api')
def api():
    return jsonify(test())

@app.route('/get_all')
def return_all():
    return jsonify(get_all())

@app.route('/get_name/<name>')
def get_name(name):
    return jsonify(get_anime())
    
@app.route('/select_type/<types>')
def select_type(types):
    return jsonify(slect_type())
    
@app.route('/name_anime')
def name_anime(names):
    return jsonify(name_anime())

@app.route('/type_anime/<type>')
def type_anime(types):
    return jsonify(type_anime())

@app.route('/link_anime/<type>')
def link_anime(link):
    return jsonify(link_anime())

if __name__ == '__main__':
    app.run(debug=True)

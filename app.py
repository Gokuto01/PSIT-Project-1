from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from route import get_all, get_name, select_type
from Google import Create_Service
import pandas as pd

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
gsheetId = '1XTmcMfTa9BLlqXfhvE4wDN0lkMaLkkzP809vb4FLKpw'

s = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
gs = s.spreadsheets()
rows = gs.values().get(spreadsheetId=gsheetId,range='Test1').execute()
data = rows.get('values')
df = pd.DataFrame(data)
print(df)

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

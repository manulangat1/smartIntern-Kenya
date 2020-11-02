from flask import Flask,jsonify
from .webscraping  import scrap_jobs
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
url= 'https://jobs.github.com/positions'
@app.route("/",methods=['GET','POST'])
def scraping():
    new = scrap_jobs(url)
    return jsonify(new)


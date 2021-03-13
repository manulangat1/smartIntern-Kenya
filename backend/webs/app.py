from flask import Flask,jsonify
# from webs.webscraping  import scrap_jobs
from . import webscraping
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
url= 'https://jobs.github.com/positions'
@app.route("/",methods=['GET','POST'])
def scraping():
    new = webscraping.scrap_jobs(url)
    return jsonify(new)

if __name__ == "__main__":
    # use 0.0.0.0 to use it in container
    app.run(host='0.0.0.0')


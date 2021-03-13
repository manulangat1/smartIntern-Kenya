from flask import Flask,jsonify
# from webs.webscraping  import scrap_jobs
from . import webscraping
from flask_cors import CORS

from rq import Queue
from rq.job import Job 
from .worker import conn
app = Flask(__name__)
CORS(app)


q = Queue(connection=conn)
url= 'https://jobs.github.com/positions'


# @app.route("/webscraping",methods=['GET','POST'])
def scraping():
    new = webscraping.scrap_jobs(url)
    return jsonify(new)

@app.route('/',methods=["GET","POST"])
def index():
    # scraping()
    # from . import scraping
    job = q.enqueue_call(
        func=scraping, result_ttl=5000
    )
    print(job.get_id())
    return jsonify("hey")

if __name__ == "__main__":
    # use 0.0.0.0 to use it in container
    app.run(host='0.0.0.0')


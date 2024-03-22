import shutil

from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request
from flask import redirect

import logging
logging.basicConfig(filename='logs/flask.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
log = logging.getLogger('EHR-ML')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', the_title="EHR-ML")


if __name__ == "__main__":
    app.run(debug=True)

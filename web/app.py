from flask import Flask
from flask import render_template

import logging
logging.basicConfig(filename='logs/flask.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
log = logging.getLogger('EHR-ML')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', the_title="EHR-ML")


@app.route('/patient', methods = ['GET', 'POST'])
def patient():
    return render_template('patient.html', the_title="EHR-ML: Patients")


if __name__ == "__main__":
    app.run(debug=True)

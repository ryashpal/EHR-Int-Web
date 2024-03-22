from flask import Flask
from flask import render_template
from flask import request

from SearchPatientUsecase import searchPatient


import logging
logging.basicConfig(filename='logs/flask.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
log = logging.getLogger('EHR-ML')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', the_title="EHR-ML")


@app.route('/patient', methods = ['GET', 'POST'])
def patient():
    if request.method == 'POST':
        patientList = searchPatient(patientId=request.form.get('patient_id'))
        return render_template('patient.html', the_title="EHR-ML: Patients", patientList=patientList)
    elif request.method == 'GET':
        return render_template('patient.html', the_title="EHR-ML: Patients")


if __name__ == "__main__":
    app.run(debug=True)

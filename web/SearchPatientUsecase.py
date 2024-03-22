import requests


def searchPatient(patientId):
    url = 'http://10.172.235.4:8080/fhir/Patient?_id=' + patientId
    response = requests.get(
        url=url
    )
    return response

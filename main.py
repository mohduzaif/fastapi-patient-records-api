from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

# open and load data from JSON file. ------> Utility Function.
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data


# home route.
@app.get('/')
def greet():
    return {
        'message' : 'Stay Happy and Healthy!'
    }


# about route.
@app.get('/about')
def about():
    return {
        'message' : "This application is actually conatin the records of all the patients!"
    }


# this route is responsible to show the data of all patients.
@app.get('/view')
def fetch_records():
    data = load_data()
    return data

# this route is responsible to show the data of specific patient according to incoming patient_id
@app.get('/patient/{patient_id}')
def fetch_patient_record(patient_id : str = Path(..., description = 'The type of the Patient is string', example = 'P001')):

    data = load_data()
    if patient_id in data:
        return data[patient_id]
        
    # this will raise an exception using HTTPException when user is not found.
    raise HTTPException(
        status_code = 400, 
        detail = f"Patient ID {patient_id} does not exist, enter the correct patient id!"
    )


@app.get('/sort')
def sort_patients(sort_by : str = Query(..., description = 'Sort the Data on the basis of height, weight and bmi'), order : str = Query('asc', description = 'Sort the data in Ascending and Descending Order')):

    valid_orders = ['height', 'weight', 'bmi']

    if sort_by not in valid_orders:
        raise HTTPException(
            status_code = 400, 
            detail = f'Input of sort_by parameter is wrong, Select from height, weight and bmi'
        )
    
    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code = 400, 
            detail = f'You passe the wrong input in order parameter, Select any one from asc and desc'
        )
    
    data = load_data()

    sorted_patients = sorted(
        data.values(),
        key = lambda patient: patient[sort_by],
        reverse=(order == "desc")
    )
    
    return sorted_patients

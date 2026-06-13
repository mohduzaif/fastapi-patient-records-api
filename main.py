from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json


# create a class for pydantic model that actually validate the data comes from the client side.
class Patient(BaseModel):
    
    patient_id : Annotated[str, Field(..., description = 'Patient Id for each patient', example = 'P001')]
    name : Annotated[str, Field(..., min_length = 3, max_length = 50, description = 'Name of the patient and lenght should be greater than 3 and less than 50', example = 'MS Dhoni')]
    city : Annotated[str, Field(..., max_length = 50, description = 'Name of city where the patient is living')]
    age : Annotated[int, Field(..., gt = 0, lt = 120, description = 'Age of the Patient')]
    gender : Literal['Male', 'Female', 'Other']
    height : Annotated[float, Field(..., gt = 0, description = 'Height of the patient in meters')] 
    weight : Annotated[float, Field(..., gt = 0, description = 'Weight of the patient')]

    # calculate bmi on the go when the validate of the data is done using pydantic model.
    @computed_field
    @property
    def bmi(self) -> float:
        calculate_bmi = round(self.weight / self.height ** 2, 2)
        return calculate_bmi
    
    # this field is calculated the verdict on the go at the time of data validation of pydantic model.
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        if 18.5 < self.bmi < 24.9:
            return 'Normal'
        if 24.9 < self.bmi < 29.9:
            return 'Overweight'
        else:
            return 'Obese'


# this pydantic model is used to validate the data comes for patient detail updation.
class PatientUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=3,
        max_length=50
    )

    city: str | None = Field(
        default=None,
        max_length=50
    )

    age: int | None = Field(
        default=None,
        gt=0,
        lt=120
    )

    gender: bool | None = Field(
        default=None
    )

    height: float | None = Field(
        default=None
    )

    weight: float | None = Field(
        default=None
    )

# create the FastAPI object to create the routes.
app = FastAPI()


# open and load data from JSON file. ------> Utility Function.
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data


# open and save data into a JSON file. ----------> Utility Function.
def save_data(data):
    with open('patients.json', 'w', encoding = 'utf-8') as f:
        json.dump(data, f, indent = 4, ensure_ascii = False)

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


# this route is responsible for the creation of new patient into the database/JSON file.
@app.post('/create')
def insert_patient(patient : Patient):

    # load the existing data from the database/JSON file.
    data = load_data()

    # check whether the given patient is already exist or not.
    if patient.patient_id in data:
        raise HTTPException(
            status_code = 400, 
            detail = f'Patient with Patient_id {patient.patient_id} is already exist in a Database.'
        )

    # insert the data into a database/JSON file.
    # extract the dictionary from the pydantic model using model_dump() by excluding patient_id due to our database structure.
    temp_data = patient.model_dump(exclude = 'patient_id')

    # stored this new patient into a actual data.
    data[patient.patient_id] = temp_data

    # save the data into a JSON file.
    save_data(data)

    # it will shows a proper status code and message to the developer who used our API.
    return JSONResponse(
        status_code = 201, 
        content = {
            'success' : True, 
            'message' : 'Patient Created Successfully'
        }
    )

# this route is responsible for the update the details of the patient into the database/JSON file.
@app.put('/update/{patient_id}')
def update_patient(patient_update : PatientUpdate, patient_id : str = Path(..., description = 'Provide the unique Id of the Patient which you want to update', example = 'P001')):
 
    # load the actual data from the JSON file.
    data = load_data()

    # check whether the given patient exist or not.
    if patient_id not in data:
        raise HTTPException(
            status_code = 404, 
            detail = 'Patient does not exist.'
        )
    
    # extract the data of that patient.
    current_patient_info = data[patient_id]
    
    # convert the pydantic object into a dictionary.
    updated_patient_info = patient_update.model_dump(exclude_unset = True)

    # update that data
    for key, value in updated_patient_info.items():
        current_patient_info[key] = value 
    
    # create the pydantic object for current updated patient.
    current_patient_info['patient_id'] = patient_id
    current_patient_obj = Patient(**current_patient_info)

    # Now convert the current patient object, because now it will contain all the info about the current patient.
    current_patient_info = current_patient_obj.model_dump(exclude = 'patient_id')

    # update the complete data that now stored to JSON file.
    data[patient_id] = current_patient_info

    # save the data to JSON file.
    save_data(data)

    # return the JSON response on sucessful updation.
    return JSONResponse(
        status_code = 200,
        content = {
            'success' : True, 
            'message' : 'Patient Data updated Successfully.'
        }
    )

# this route is responsible for the deletion of the patient information from the database/JSON file.
@app.delete('/delete_patient/{patient_id}')
def delete_patient(patient_id : str = Path(..., description = 'Provide the unique Id of the Patient which you want to delete from the database', example = 'P001')):
    
    # load the data.
    data = load_data()

    # check whether the given patient exist or not.
    if patient_id not in data:
        raise HTTPException(
            status_code = 404, 
            detail = 'Patient does not Exist.'
        )
    
    # delete the user from the current data.
    del data[patient_id]

    # Stored back the new data into a database/JSON file 
    save_data(data)

    # return the JSON response on sucessful updation.
    return JSONResponse(
        status_code = 200,
        content = {
            'success' : True, 
            'message' : 'Patient Data deleted Successfully.'
        }
    )

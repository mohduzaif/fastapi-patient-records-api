from pydantic import BaseModel, EmailStr, Field, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    # here we mentioned all the fields are required.
    name : str
    email : EmailStr
    age : Annotated[int, Field(gt = 0)]
    weight : float
    height : float
    married : bool = False
    contact_details : Dict[str, str]

    # this is the field that we make it optional but we need to set a default value in it. 
    allergies : Optional[List[str]] = None

    # computed_field() is used to calculate the fields on the go when we create a pydnatic model. 
    @computed_field
    @property
    def bmi(self) -> float:
        calculate_bmi = round(self.weight / (self.height ** 2), 2)
        
        return calculate_bmi


def update_data_into_DB(patient : Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

    print('Data has been Updated Successfully!')

dictionary = {
    'name' : 'huzaifa', 
    'email' : 'abc@icici.com',
    'age' : 16, 
    'weight' : 60.0, 
    'height' : 1.78,
    'allergies' : ['dast', 'pllen'], 
    'contact_details' : {
        'phone_no' : '1234567898',
        'emergency' : '678965'
    }
} 


# here we dont need to unpack the dictionary, because model_validate function.
patient = Patient.model_validate(dictionary)

update_data_into_DB(patient)


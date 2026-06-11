from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated


# model_validator() is used when validation depends on multiple fields together, not just a single field.

# Think of it this way:
    # field_validator() → validates one field at a time.
    # model_validator() → validates the entire model (all fields together).


class Patient(BaseModel):

    # here we mentioned all the fields are required.
    name : str
    email : EmailStr
    age : Annotated[int, Field(gt = 0)]
    weight : float
    married : bool = False
    contact_details : Dict[str, str]

    # this is the field that we make it optional but we need to set a default value in it. 
    allergies : Optional[List[str]] = None

    # check whether a patient age more than 60 and less than 18, it must having emergency contact number.
    # here the validation is required on both the fields, so here it require model_validator().
    @model_validator(mode = 'after')
    def validate_patient_details(model):

        if (model.age < 18 or model.age > 60) and 'emergency' not in model.contact_details:
            raise ValueError('Patient must have an Emergency contact number having age less than 18 and greater than 60')
        
        return model
    

    # check whether name is only contain alphabets not numeric value.
    @field_validator('name')
    @classmethod
    def name_validator_and_transform(cls, value_name):

        if not value_name.isalpha():
            raise ValueError('Name containing the numeric values..!')
        
        return value_name.upper()
    
    # check whether the email belong to specific type of domain.
    # field_validator works in 2 mode(before and after)
    @field_validator('email', mode = 'after')
    @classmethod
    def email_validator(cls, value_email):

        valid_domains = ['hdfc.com', 'icici.com', 'axis.com']

        input_domain = value_email.split('@')[-1]

        if input_domain not in valid_domains:
            raise ValueError('Incorrect input domain..!')
        
        return value_email


def insert_data_into_DB(patient : Patient):

    print('See the name in capital letter : ', patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

    print('Data has been Inserted Successfully!')

def update_data_into_DB(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)

    print('Data has been Updated Successfully!')

dictionary = {
    'name' : 'huzaifa', 
    'email' : 'abc@icici.com',
    'age' : 16, 
    'weight' : 62.4, 
    'allergies' : ['dast', 'pllen'], 
    'contact_details' : {
        'phone_no' : '1234567898',
        'emergency' : '678965'
    }
} 


# here we dont need to unpack the dictionary, because model_validate function.
patient = Patient.model_validate(dictionary)

insert_data_into_DB(patient)
# update_data_into_DB(patient)


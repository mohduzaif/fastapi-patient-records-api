from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


# field_validator() is used when the built-in validations provided by Field() are not enough and you need to write custom validation logic for one or more fields.

# examples where we need a field_validator
# Name must contain only alphabets.
# Email must belong to a specific domain.
# Age must be at least 18.
# Password must contain a special character.
# Weight must be realistic for a human.

# These require custom logic, so we use field_validator().


class Patient(BaseModel):

    # here we mentioned all the fields are required.
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool = False
    contact_details : Dict[str, str]

    # this is the field that we make it optional but we need to set a default value in it. 
    allergies : Optional[List[str]] = None
    

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
    'age' : 25, 
    'weight' : 62.4, 
    'allergies' : ['dast', 'pllen'], 
    'contact_details' : {
        'phone_no' : '1234567898'
    }
} 


# here we dont need to unpack the dictionary, because model_validate function.
patient = Patient.model_validate(dictionary)

insert_data_into_DB(patient)
# update_data_into_DB(patient)


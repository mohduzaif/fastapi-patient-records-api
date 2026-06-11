from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    # name : str = Field(max_length = 50)
    # Annotated is responsible for the type as well as the meta data of the field.
    name : Annotated[str, Field(min_length = 3, max_length = 50, title = 'Patient Name', description = 'The name of the patient should have a length greater than 3 and less than 50.')]

    email : EmailStr
    website : AnyUrl
    
    age : Annotated[int, Field(gt = 0, lt = 120, title = 'Patient Age', description = 'The Age of the patient is greater than 0 and less than 120.')]
    
    # strict keyword responsible for the type coercion, means convert to corrct data type whenever required.
    weight : Annotated[float, Field(gt = 0, strict = True)]
    married : bool = False
    contact_details : Dict[str, str]
    allergies : Optional[List[str]] = None
    



def insert_data_into_DB(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.website)
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
    'name' : 'uzaif', 
    'email' : 'abc@xyz.com',
    'website' : 'https://www.google.com',
    'age' : 25, 
    'weight' : 62.4, 
    'allergies' : ['dast', 'pllen'], 
    'contact_details' : {
        'phone_no' : '1234567898',
        'address' : 'New York'
    }
} 

# here we dont need to unpack the dictionary, because model_validate function.
patient = Patient.model_validate(dictionary)

insert_data_into_DB(patient)
# update_data_into_DB(patient)


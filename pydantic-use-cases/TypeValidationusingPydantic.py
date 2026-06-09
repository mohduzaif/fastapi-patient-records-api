from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):

    # here we mentioned all the fields are required.
    name : str
    age : int
    weight : float
    married : bool = False
    contact_details : Dict[str, str]

    # this is the field that we make it optional but we need to set a default value in it. 
    allergies : Optional[List[str]] = None
    


# here we clearly see that we dont need to write similar code again again in the different function.
# code reusibity increase.
def insert_data_into_DB(patient : Patient):

    print(patient.name)
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
    'name' : 'uzaif', 
    'age' : 25, 
    'weight' : 62.4, 
    # 'allergies' : ['dast', 'pllen'], 
    'contact_details' : {
        'email' : 'abc@gmail.com', 
        'phone_no' : '1234567898'
    }
} 

# here we are unpack the dictionary first before passing it.
# patient = Patient.model_validate(**dictionary)

# here we dont need to unpack the dictionary, because model_validate function.
patient = Patient.model_validate(dictionary)

insert_data_into_DB(patient)
# update_data_into_DB(patient)


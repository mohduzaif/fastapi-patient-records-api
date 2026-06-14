from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd


# import the machine-learning model.
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# create the object of the FastAPI
app1 = FastAPI()

# list of cities according the tiers.
tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]

tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]


# create the pydantic model for the data validation coming from the user.
class UserInput(BaseModel):

    age : Annotated[
        int, Field(..., gt = 0, description = 'Age of the user and it should be grater than 0', examples = [23])
    ]
    weight : Annotated[
        float, Field(..., gt = 0, description = 'Weight of the user and it also greater than 0 and also in kgs', examples = [45.5])
    ]
    height : Annotated[
        float,  Field(..., gt = 0, description = 'Height of the user and it should be greater than 0 and also in meters', examples = [170.4])
    ] 
    income_lpa : Annotated[
        float, Field(..., gt = 0, description = 'Income of the user and it also graeter than 0 and it is in LPA', examples = [14.56])
    ] 
    smoker : Annotated[
        bool, Field(description = 'Is the person is a smoker or not')
    ]
    city : Annotated[
        str, Field(..., max_length = 50, description = 'City of the user to which it belongs', examples = ['New Delhi'])
    ]
    occupation : Annotated[
        Literal['retired', 'freelancer', 'student', 'government_job',
        'business_owner', 'unemployed', 'private_job'], Field(description = 'Occupation of the user')
    ]

    # this computed field is calculated the bmi.
    @computed_field
    @property
    def bmi(self) -> float:
        calculate_bmi = self.weight / (self.height ** 2)
        return calculate_bmi 

    # this computed field is calculate the age_group of the user.
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"


    # this computed field is responsible for find their city_tier
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        

    # this computed field is responsible for find life_style_risk
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker and self.bmi > 27:
            return "medium"
        else:
            return "low"

@app1.get('/')
def home():
    return {
        'message' : 'Hey this is the end-points for Incurance related issues.'
    }

# create an end-point for the prediction
@app1.post('/predict', summary="Predict Diabetes Risk",
    description="This endpoint accepts user health and demographic data and returns the predicted diabetes risk."
)
def predicted_result(userData : UserInput):
    
    current_input_df = pd.DataFrame([{
        'bmi' : userData.bmi, 
        'age_group' : userData.age_group, 
        'lifestyle_risk' : userData.lifestyle_risk, 
        'city_tier' : userData.city_tier, 
        'income_lpa' : userData.income_lpa, 
        'occupation' : userData.occupation
    }])

    prediction = model.predict(current_input_df)[0]


    return JSONResponse(
        status_code=200, content={'predicted_category': prediction}
    )


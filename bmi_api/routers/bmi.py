from pydantic import BaseModel, Field
from fastapi import APIRouter, Body
from typing import Annotated
from datetime import datetime


class BMI(BaseModel):
    bmi: float = Field(title="BMI")
    description: str = Field(title="Description")
    check_at: str | None = Field(title="BMI Check at")


class BMIInput(BaseModel):
    height: str = Field(title="Enter Height in cms")
    weight: str = Field(title="Enter Weight in kgs")


router = APIRouter(
    prefix="/api",
    tags=["bmi"],
)


@router.post(path="/bmi")
def get_bmi(bmi_input: Annotated[BMIInput, Body(..., embed=True)]):
    height = float(bmi_input.height) / 100
    weight = float(bmi_input.weight)
    bmi = weight / (height**2)
    if bmi < 18.5:
        bmi_check = "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_check = "Normal weight"
    elif bmi >= 25 and bmi <= 29.9:
        bmi_check = "Overweight"
    elif bmi >= 30 and bmi <= 34.9:
        bmi_check = "Obesity Class I"
    elif bmi >= 35 and bmi <= 39.9:
        bmi_check = "Obesity Class II"
    elif bmi >= 40:
        bmi_check = "Obesity Class III"
    bmi = BMI(
        bmi=bmi,
        description=bmi_check,
        check_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    return {
        "status": "success",
        "message": "BMI calculated successfully",
        "data": bmi,
    }

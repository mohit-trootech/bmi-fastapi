from pydantic import BaseModel, Field, field_validator
from fastapi import Path, Body, Query, APIRouter
from typing import Annotated


class User(BaseModel):
    name: str = Field(title="User's Full Name")
    email: str | None = Field(title="User Email Address")

    @field_validator("email")
    def validate_email_field(cls, value):
        if value:
            if "@" not in value:
                raise ValueError("Invalid Email Address")
        return value


class UserMetaData(BaseModel):
    height: str = Field(title="Enter Height in cms")
    weight: str = Field(title="Enter Weight in kgs")


class BMI(BaseModel):
    bmi: str = Field(title="BMI")
    check_at: str | None = Field(title="BMI Check at")


router = APIRouter(
    prefix="/api",
    tags=["bmi"],
)


@router.post(path="/")
async def get_user_data(
    name: str,
    user: Annotated[User, Body(embed=True)],
):
    return user

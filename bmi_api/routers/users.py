from pydantic import BaseModel, Field, field_validator
from fastapi import Body, APIRouter, exceptions, Path
from typing import Annotated
from email_validator import EmailNotValidError, validate_email
from ..dependencies import (
    get_users_from_username,
    create_user_firestore,
    get_users_data,
    delete_user_firestore,
    filter_users_from_username,
)


class User(BaseModel):
    username: str = Field(title="Username")
    name: str = Field(title="Full Name")
    email: str | None = Field(title="Email Address")

    @field_validator("email")
    def validate_email(cls, value):
        """
        Validate Email - have @ and a `.` in value.
        """
        try:
            validate_email(value)
        except EmailNotValidError as err:
            raise ValueError(f"invalid email: {err}") from None
        return value

    @field_validator("username")
    def validate_username(cls, value):
        """
        Validate Username - must be alphanumeric and no space in between
        """
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric")
        return value


router = APIRouter(
    prefix="/api",
    tags=["users"],
)


@router.get(path="/users")
async def get_users(
    username: Annotated[str, Field(description="Enter Username")] = None
):
    if username:
        users_data = filter_users_from_username(username=username)
    else:
        users_data = get_users_data()
    if not users_data:
        raise exceptions.HTTPException(status_code=404, detail="No users found")
    return {
        "status": "success",
        "message": "Users fetched successfully",
        "data": users_data,
    }


@router.post(path="/users")
async def create_user(user: User = Body(embed=True)):
    user_data = create_user_firestore(user=user)
    if not user_data:
        raise exceptions.HTTPException(status_code=400, detail="User creation failed")
    return {
        "status": "success",
        "message": "User created successfully",
        "data": user_data,
    }


@router.get(path="/users/{username}")
async def get_user_details(username: str = Path(..., description="The username")):
    user_data = get_users_from_username(username=username)
    if not user_data:
        raise exceptions.HTTPException(status_code=404, detail="No users found")
    return {
        "status": "success",
        "message": "User fetched successfully",
        "data": user_data,
    }


@router.put(path="/users/{username}")
async def update_user(username: str, user: User = Body(embed=True)):
    user_data = create_user_firestore(user=user)
    if not user_data:
        raise exceptions.HTTPException(status_code=400, detail="User updation failed")
    return {
        "status": "success",
        "message": "User updated successfully",
        "data": user_data,
    }


@router.delete(path="/users/{username}")
async def delete_user(username: str = Path(..., description="The username to delete")):
    try:
        delete_user_firestore(username=username)
        return {"status": "success", "message": "User deleted successfully"}
    except Exception:
        raise exceptions.HTTPException(status_code=400, detail="User deletion failed")

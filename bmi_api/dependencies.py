from .internal.firebase import db
from google.cloud.firestore import FieldFilter

users = db.collection("users")


def get_users_data() -> dict:
    """
    This function fetches all users data from firestore.
    """
    try:
        results = users.stream()
        users_data = [doc.to_dict() for doc in results]
        return users_data
    except Exception:
        return None


def create_user_firestore(user: dict) -> None:
    """
    This function takes user details as input and stores it in firestore.
    user_ref = users.document(user.name)
    user_ref.set(user.dict())
    :param user: _description_
    """
    try:
        users.document(user.username).set(user.dict())
        return user.dict()
    except Exception:
        return None


def filter_users_from_username(username: str):
    """
    This function takes username as input and returns the user details from firestore.
    query = users.where("username", "==", username)
    results = query.stream()
    user_details = [doc.to_dict() for doc in results]
    :param username: str
    :return: list
    """
    query = users.where(filter=FieldFilter("username", "<=", username))
    results = query.stream()
    return [doc.to_dict() for doc in results]


def get_users_from_username(username: str):
    """
    This function takes username as input and returns the user details from firestore.
    query = users.where("username", "==", username)
    results = query.stream()
    user_details = [doc.to_dict() for doc in results]
    :param username: str
    :return: list
    """
    query = users.where(filter=FieldFilter("username", "==", username))
    results = query.stream()
    return [doc.to_dict() for doc in results]


def delete_user_firestore(username: str):
    """
    This function takes username as input and deletes the user from firestore.
    """
    try:
        users.document(username).delete()
    except Exception:
        return None

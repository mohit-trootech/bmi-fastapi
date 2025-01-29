import firebase_admin
from firebase_admin import firestore, credentials
from ..conf.settings import SERVICE_KEY

cred = credentials.Certificate(SERVICE_KEY)
firebase_admin.initialize_app(cred)
db = firestore.client()

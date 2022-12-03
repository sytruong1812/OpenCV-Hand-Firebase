import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('Firebase-SDK.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hand-opencv-esp-default-rtdb.firebaseio.com/'
})

ref = db.reference('Control')
ref.update({
    'LED': 1
})

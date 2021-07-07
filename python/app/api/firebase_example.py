from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import time

# Initilizing

cred = credentials.Certificate(
    "my_api.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://minh-2b2f4.firebaseio.com/'
})
# key = "-L8SwnVwWKy3sOUVnBET"
key = "-L8T8T6rbBAGPt2p9FeE"

# Get info from firebase
def read_firebase(key):
	ref = db.reference(key) #database
	return ref.get()

# Write data to firebase
def write_firebase(key,data):
    ref = db.reference(key)
    ref.update(info)
    print("Write done")
# Main
dt = read_firebase(key)
print(dt)
# then write something
info = {
"key1":"value1",
"key2":"value2"
}
write_firebase(key,info)
dt = read_firebase(key)
print(dt)
# Output
# {'message': 'Xin chao', 'name': 'Test1'}
# Write done
# {'key1': 'value1', 'key2': 'value2', 'message': 'Xin chao', 'name': 'Test1'}


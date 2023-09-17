import firebase_admin
from firebase_admin import credentials, db
#setting a real time database
cred = credentials.Certificate("ficeattendancerealtime-firebase-adminsdk-t4txi-676cfc11fc.json") #ENTER YOUR OWN DATABASE KEY
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://ficeattendancerealtime-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "123432" :
        {
            "name": "Erka",
            "major": "Computer sience",
            "starting_year" : 2017,
            "total_attendance":6,
            "standing": "G",
            "Year":4,
            "last_attendance" : "2022-12-11 00:51:32"


        }
}
for k,v in data.items():
    ref.child(k).set(v)
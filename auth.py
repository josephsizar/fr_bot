import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDqCFLWUbO5FgqCLmd8HC5no-Uo8RK3TqI",

  'authDomain': "fire-bot-82e38.firebaseapp.com",

  'projectId': "fire-bot-82e38",

  'storageBucket': "fire-bot-82e38.appspot.com",

  'messagingSenderId': "500767818130",

  'appId': "1:500767818130:web:c58c9dfed45a379901414b",

  'measurementId': "G-RN3WT66257"

}

firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def signup():
    print("================== welcome to register bot ===================")
    email=input("Enter Email :")
    password = input("Enter Password : ")
    user = auth.create_user_with_email_and_password(email,password)


signup()


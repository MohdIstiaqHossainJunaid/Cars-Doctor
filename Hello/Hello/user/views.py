from django.shortcuts import render
import pyrebase
from django.contrib import auth
config = {

'apiKey': "AIzaSyDIPYvyKKLSapsyZDtQNog8SKw9WY98CcE",
    'authDomain': "cpanel-5e873.firebaseapp.com",
    'databaseURL': "https://cse327-nbm-38793-default-rtdb.firebaseio.com/",
    'projectId': "cse327-nbm-38793",
    'storageBucket': "cse327-nbm-38793.appspot.com",
    'messagingSenderId': "984927104831"
  }

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database=firebase.database()
def signIn(request):

    return render(request, "signIn.html")
def postsignx(request):

    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credentials"
        return render(request,"signIn.html",{"messg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    if not 'uid' in request.session:
        return render(request, 'signIn.html')
    else:

        return render(request, "index.html")

def back(request):
    return render(request, "Userdash.html")

def logout(request):
    auth.logout(request)
    return render(request,'signIn.html')


def signup(request):

    return render(request,"signup.html")


def postsignup(request):

    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
        message="Successfully created account"
    except:
        message="Error"
        return render(request,"signup.html",{"messg":message})
        uid = user['localId']

    data={"name":name,"status":"1"}

    database.child("users").child("uid").child("details").set(data)
    return render(request,"signIn.html")
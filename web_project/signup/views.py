from django.shortcuts import render
import mysql.connector as sql
fn = ''
ln = ''
s = ''
em = ''
pwd = ''
# Create your views here.
def signup(request):
    global fn, ln, s, em, pwd
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", passwd="Manoj@2310", database="website")
        cursor= m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="First_Name":
                fn==value
            if key=="Last_Name":
                ln==value
            if key=="sex":
                s==value
            if key=="email":
                em==value
            if key=="password":
                pwd==value
        
        c="insert into users values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()
    
    return render(request, 'signup.html')
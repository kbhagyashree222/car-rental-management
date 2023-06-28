from optparse import Values
from django.shortcuts import render
import mysql.connector as sql

tn=''
fn=''
ln=''
mo=''
em=''
pwd=''
# Create your views here.
def registrationaction(request):
    global tn,fn,ln,mo,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="mysql123",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="type":
                tn=value
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="mobile":
                mo=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        if tn =="customer":
          c="insert into register values('{}','{}','{}','{}','{}','{}')".format (tn,fn,ln,mo,em,pwd)
        else:
          c="insert into driver_register values('{}','{}','{}','{}','{}','{}')".format (tn,fn,ln,mo,em,pwd)  

        cursor.execute(c)
        m.commit()

    return render(request,'registration.html')

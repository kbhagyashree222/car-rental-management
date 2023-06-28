from django.shortcuts import render
import mysql.connector as sql
tn=''
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global tn,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="mysql123",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="type":
                tn=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from register where type='{}' and email='{}' and password='{}'".format(tn,em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        n=len(t)
        i=tn
        if t==():
            return render(request,'error.html')
        else:
            if i=='Customer':
                return render(request,"customer.html")
            else:
                return render(request,"welcome.html")

    return render(request,'login.html')

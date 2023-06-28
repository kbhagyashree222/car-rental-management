from optparse import Values
from django.shortcuts import render
import mysql.connector as sql
tn=''
ft=''
dn=''
dt=''
em=''
mo=''
# Create your views here.
def driveraction(request):
    global tn,ft,dn,dt,em,mo
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="mysql123",database='website')
        cursor=m.cursor()
        a=request.POST
        for key,value in a.items():
            if key=="type":
                tn=value
            if key=="from the":
                ft=value
            if key=="destination":
                dn=value
            if key=="edate":
                dt=value
            if key=="email":
                em=value
            if key=="mobile":
                mo=value
        
        c="insert into driver values('{}','{}','{}','{}','{}','{}')".format (tn,ft,dn,dt,em,mo)
        cursor.execute(c)
        m.commit()

    return render(request,'driver.html')

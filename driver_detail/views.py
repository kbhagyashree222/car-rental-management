from optparse import Values
from django.shortcuts import render
import mysql.connector as sql
em=''
dis=''
dob=''
ag=''
ad=''
lic=''
liex=''
ft=''
v_no=''
puc=''
ins=''
v_d=''
v_dx=''
ac=''
v_t=''
v_n=''
v_c=''
rc=''
# Create your views here.
def detailaction(request):
    global em,dis,dob,ag,ad,lic,liex,ft,v_no,puc,ins,v_d,v_dx,ac,v_t,v_n,v_c,rc
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="mysql123",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="type":
                dis=value
            if key=="dob":
                dob=value
            if key=="age":
                ag=value
            if key=="addr":
                ad=value
            if key=="licence":
                lic=value
            if key=="licence_exp":
                liex=value
            if key=="fasttag":
                ft=value
            if key=="vehicle_no":
                v_no=value
            if key=="puc":
               puc =value
            if key=="insurance":
                ins=value
            if key=="v_dop":
                v_d=value
            if key=="v_doexp":
                v_dx=value
            if key=="ac":
                ac=value
            if key=="v_type":
                v_t=value
            if key=="v_name":
                v_n=value
            if key=="v_company":
                v_c=value
            if key=="rc":
                rc=value
            if key=="email":
                em=value




        c="insert into driver_detail values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format (dis,dob,ag,ad,lic,liex,ft,v_no,puc,ins,v_d,v_dx,ac,v_t,v_n,v_c,rc,em)  

        cursor.execute(c)
        m.commit()

    return render(request,'driver_detail.html')

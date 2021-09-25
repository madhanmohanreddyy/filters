from django.shortcuts import render
import datetime

# Create your views here.
def madhu(request):
    data='madhan mohan reddy ravulacheruvu'
    date1=datetime.datetime.now()
    return render(request,'madhu.html',context={'data':data,'date1':date1,'count':10})
    
def user(request):
    data='MADHAN mohan reddy mohan'
    return render(request,'user.html',context={'data':data})
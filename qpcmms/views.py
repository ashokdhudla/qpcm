# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import card
from django.shortcuts import render_to_response,HttpResponseRedirect
import datetime

def index(request):
       
    return render_to_response('index.html')
    
def members(request):
       
    return render_to_response('members.html')
    
def users(request):
       
    return render_to_response('users.html')
    
def common(request):
       
    return render_to_response('common.html')
    
def reports(request):    
    obj_list = card.objects.all()       
    txn_list=[]
    for i in range(len(obj_list)):
        dic = {}        
        dic['id'] = obj_list[i].id
        dic['cardid'] = obj_list[i].cardid
        dic['datetime'] = str(obj_list[i].datetime)        
        txn_list.append(dic)
    
    return render_to_response('reports.html',{'report_list':txn_list})
    



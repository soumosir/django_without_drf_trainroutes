

from django.http import JsonResponse
import json
from . import models
from django.db.models import Q
import time

# Create your views here.
def index(requests):

    print(" iwbiwbiwbivwb ",requests.GET)
    user_filter = {
    "source" : requests.GET.getlist('source') if requests.GET.__contains__('source') else False,
    "destination" : requests.GET.getlist('destination') if requests.GET.__contains__('destination') else False,
    "start_day" : requests.GET.getlist('start_day') if requests.GET.__contains__('start_day') else False,
    "reached_day" : requests.GET.getlist('end_day') if requests.GET.__contains__('end_day') else False,
    "start_time_quarter" : requests.GET.getlist('start_time_quarter') if requests.GET.__contains__('start_time_quarter') else False,
    "reached_time_quarter" : requests.GET.getlist('reached_time_quarter') if requests.GET.__contains__('reached_time_quarter') else False,
    "train_class" : requests.GET.getlist('train_class') if requests.GET.__contains__('train_class') else False,
    }     



    print(user_filter)
    q_objects = Q() # Create an empty Q object to start with
    # for t in train_class:
    #     q_objects |= Q(Train__train_class__contains=t)

    
    if user_filter["source"]:
        q_objects &= Q(source__contains=user_filter["source"][0])    
    if user_filter["destination"]:
        q_objects &= Q(destination__contains=user_filter["destination"][0])  
    if user_filter["start_day"]:
        q_objects &= Q(start_day__contains=user_filter["start_day"][0])    
    if user_filter["reached_day"]:
        q_objects &= Q(reached_day__contains=user_filter["reached_day"][0])   
    if user_filter["start_time_quarter"]:
        
        if user_filter["start_time_quarter"][0]=='0':
            q_objects &= Q(start_time__gte='00:00:00',start_time__lte='05:59:59') 
        elif user_filter["start_time_quarter"][0]=='1':
            q_objects &= Q(start_time__gte='06:00:00',start_time__lte='11:59:59')  
        elif user_filter["start_time_quarter"][0]=='2':
            q_objects &= Q(start_time__gte='12:00:00',start_time__lte='17:59:59') 
        elif user_filter["start_time_quarter"][0]=='3':
            q_objects &= Q(start_time__gte='18:00:00',start_time__lte='23:59:59') 

    if user_filter["reached_time_quarter"]:

        if user_filter["reached_time_quarter"][0]=='0':
            q_objects &= Q(reached_time__gte='00:00:00',reached_time__lte='05:59:59') 
        elif user_filter["reached_time_quarter"][0]=='1':
            q_objects &= Q(reached_time__gte='06:00:00',reached_time__lte='11:59:59')  
        elif user_filter["reached_time_quarter"][0]=='2':
            q_objects &= Q(reached_time__gte='12:00:00',reached_time__lte='17:59:59') 
        elif user_filter["reached_time_quarter"][0]=='3':
            q_objects &= Q(reached_time__gte='18:00:00',reached_time__lte='23:59:59') 
              

    if user_filter["train_class"]:
        i=0
        for t_c in user_filter["train_class"]:
            i+=1
            if i==1:
                q_inner_objects = Q(train__train_class__contains=user_filter["train_class"][i-1])    
            else:
                q_inner_objects |= Q(train__train_class__contains=user_filter["train_class"][i-1])  

        q_objects &= q_inner_objects   


    print(q_objects) 
    trainroutes = models.TrainRoute.objects.filter(q_objects)

   
    data =  list(trainroutes.values("id",
                                "train",
                                "start_day",
                                "start_time",
                                "reached_day",
                                "reached_time",
                                "source",
                                "destination",
                                "duration"
                                ))
    if len(data):                                
        return JsonResponse({'statusCode':200, 'data':data  })
    else:
        return JsonResponse({'statusCode':404, 'data':"No data found for your request"  })



def traindetails(requests,train_id):
    try:
        train = models.Train.objects.filter(pk=train_id)
        data = list(train.values("id","train_number","train_name","train_path","train_class","days"))
       
        return JsonResponse({'statusCode':200, 'data':data[0]})
    
    except Exception as identifier:
            
        return JsonResponse({'statusCode':404, 'data':"No data found for your request"})

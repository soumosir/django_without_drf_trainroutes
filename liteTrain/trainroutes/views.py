

from django.http import JsonResponse
import json
from . import models

# Create your views here.
def index(requests):

    # routes = models.Route.objects.all()
    # data1 =  list(routes.values("id",
    #                             "src_id",
    #                             "dest_id",
    #                             "distance",
    #                             ))
    # trainroutes = models.TrainRoute.objects.all()
    # data2 =  list(trainroutes.values("id",
    #                             "train_id",
    #                             "route_id",
    #                             "start_time",
    #                             'duration'
    #                             ))
    # trains = models.Train.objects.all()
    # data3 =  list(trains.values("id",
    #                             "train_number"
    #                             "train_name",
    #                             "train_path",
    #                             "start_time",
    #                             'total_duration',
    #                             'train_class',
    #                             'days'
    #                             ))             

    # stations = models.Station.objects.all()
    # data4 =  list(trains.values("id",
    #                             "station_name"
    #                             ))                                              
    return JsonResponse({'response':200, 'data1':data1 ,'data2':data2 ,'data3':data3, 'data4':data4  })
    

def traindetails(requests,train_id):
    try:
        train = models.Train.objects.filter(pk=train_id)
        data = list(train.values("id","train_name","train_path",'start_time','total_duration'))
        # print(data)
        return JsonResponse({'response':200, 'data':data[0]})
    
    except Exception as identifier:
            
        return JsonResponse({'response':404, 'message':str(identifier)})

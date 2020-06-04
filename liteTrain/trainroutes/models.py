from django.db import models
# Create your models here.
class Train(models.Model):

    train_class_types = (('RJ', 'Rajdhani'),
                        ('PS', 'Passenger'),
                        ('SD', 'Satabdi'),)
    train_number = models.IntegerField(unique=True)
    train_name = models.CharField(max_length=256,unique=True)
    train_path = models.CharField(max_length=256)
    start_time = models.TimeField()
    total_duration = models.TimeField()
    train_class = models.CharField(max_length=2,choices=train_class_types,default='PS',)
    days = models.CharField(max_length=10)



    def __str__(self):
        return str(self.id) + " --- " + self.train_name

class Station(models.Model):

    station_name = models.CharField(max_length=256,unique=True)
    def __str__(self):
        return str(self.id) +" -- "+self.station_name

class Route(models.Model):

    src_id = models.ForeignKey(Station, related_name='srcidtostation' ,on_delete=models.CASCADE)
    dest_id = models.ForeignKey(Station, related_name='destidtostation',on_delete=models.CASCADE)
    distance = models.FloatField(blank=False)
    def __str__(self):
        return str(self.id) + " -- "+ str(self.src_id) + " -- " + str(self.dest_id)


class TrainRoute(models.Model):

    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    start = models.TimeField(auto_now=False,auto_now_add=False)
    duration = models.TimeField(auto_now=False,auto_now_add=False)
    def __str__(self):
        return str(self.id) +" -- "+ str(self.train_id) + " -- "+str(self.route_id)




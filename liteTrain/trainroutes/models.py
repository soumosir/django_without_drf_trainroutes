from django.db import models
# Create your models here.
class Train(models.Model):

    train_class_types = (('RJ', 'Rajdhani'),
                        ('PS', 'Passenger'),
                        ('SD', 'Satabdi'),)
    train_number = models.IntegerField(unique=True)
    train_name = models.CharField(max_length=256,unique=True)
    train_path = models.CharField(max_length=256)
    train_class = models.CharField(max_length=2,choices=train_class_types,default='PS',)
    days = models.CharField(max_length=10)



    def __str__(self):
        return str(self.id) + " --- " + self.train_name


class TrainRoute(models.Model):

    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    start_day = models.IntegerField()
    reached_day = models.IntegerField()
    start_time = models.TimeField(auto_now=False,auto_now_add=False)
    reached_time = models.TimeField(auto_now=False,auto_now_add=False)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    duration = models.TimeField(auto_now=False,auto_now_add=False)

    class Meta:
        ordering = ('duration', )

    def __str__(self):
        return str(self.id) +" -- "+ str(self.train) + " -- "+str(self.start_day)




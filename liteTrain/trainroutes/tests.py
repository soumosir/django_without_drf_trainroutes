from django.test import TestCase

from . import models
# Create your tests here.



class TrainRoutesTestCase(TestCase):
    def setUp(self):
        pass

    def test_train_db(self):
        
        
        train = models.Train.objects.filter(pk=train_id)
        data = list(train.values("id","train_number","train_name","train_path","train_class","days"))

        real_value =  [{
            "id": 1,
            "train_number": 12345,
            "train_name": "Bangalore-Chennai-DoubleDecker",
            "train_path": "Bangalore(6.00hrs)-Vellore(9.00hrs)-Chennai(11.00hrs)",
            "train_class": "SD",
            "days": "WWWNWWN"
        }]
        

        
        self.assertEqual(data, real_value)

    def test_trainroutes_db(self):
        trainroutes = models.TrainRoute.objects.all()
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
        
        real_value =  [{
                        "id": 3,
                        "train": 2,
                        "start_day": 0,
                        "start_time": "13:00:00",
                        "reached_day": 0,
                        "reached_time": "14:30:00",
                        "source": "bengaluru",
                        "destination": "vellore",
                        "duration": "01:30:00"
                        },
                        {
                        "id": 2,
                        "train": 1,
                        "start_day": 0,
                        "start_time": "09:00:00",
                        "reached_day": 0,
                        "reached_time": "11:00:00",
                        "source": "vellore",
                        "destination": "chennai",
                        "duration": "02:00:00"
                        },
                        {
                        "id": 1,
                        "train": 1,
                        "start_day": 0,
                        "start_time": "06:00:00",
                        "reached_day": 0,
                        "reached_time": "09:00:00",
                        "source": "bengaluru",
                        "destination": "vellore",
                        "duration": "03:00:00"
                        }]
                            
        self.assertEqual(data, real_value)
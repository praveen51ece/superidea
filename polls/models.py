from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


class Client(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=11, blank=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=11, blank=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50, blank=True)  # Field name made lowercase.
    display = models.IntegerField(default=1)   
    cli_isused = models.IntegerField(default=0)    


    class Meta:
        managed = False
        db_table = 'CLIENT'











































# class Question(models.Model):
#     # ...
#     def __str__(self):
#         return self.question_text
# class Choice(models.Model):
#     # ...
#     def __str__(self):
#         return self.choice_text  
# class Question(models.Model):
#     # ...
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)     
        
# 

    


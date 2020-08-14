from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    studentname=models.CharField(max_length=50)
    studentemail=models.CharField(max_length=50)
    studentphone=models.IntegerField()
    studentage=models.IntegerField()
    studentrollno=models.IntegerField()
    studentgender=models.CharField(max_length=50)
    image=models.URLField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.studentname
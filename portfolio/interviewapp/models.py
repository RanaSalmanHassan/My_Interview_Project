from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Interview(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_interview')
    date = models.DateField(blank=False)
    activities = models.TextField(blank=True)
    no_of_Hours = models.PositiveIntegerField(blank=False)
    positon_of_interviewd_person = models.CharField(max_length=500,blank=False)
    marks = models.PositiveIntegerField(blank=False,validators=[MaxValueValidator(10),MinValueValidator(0)])
    comments = models.TextField(blank=True)
    attachments = models.FileField(upload_to='attachments',blank=True)
    refer = models.BooleanField(default=False)

    def __str__(self):
        return ('{}'.format(self.date))
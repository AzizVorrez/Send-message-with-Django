from django.db import models

class Message(models.Model):
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=1000)
    mdate = models.DateTimeField(auto_now_add=True)
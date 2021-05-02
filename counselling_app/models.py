from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    counsellor = models.CharField(max_length= 100)
    date = models.CharField(max_length= 100)
    subject = models.TextField()

    def __str__(self):
        return f"{self.user.username} {self.subject}"

class OTP(models.Model):
    code = models.IntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = "OTP code"
        verbose_name_plural = "OTP codes"
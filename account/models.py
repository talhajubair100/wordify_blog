from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    phone = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

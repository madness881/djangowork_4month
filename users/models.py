from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Profile(models.Model):
    age = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

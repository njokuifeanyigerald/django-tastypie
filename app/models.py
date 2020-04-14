from django.db import models
from django.contrib.auth.models import User
from tastypie.utils.timezone import now


class Myway(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title =  models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=now)

    class Meta:
        verbose_name_plural = "my ways"
    def __str__(self):
        return self.title
    
from django.db import models


# DB를 조작하는 methods들이 models.Model에 존재한다.
class Addresses(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    data_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


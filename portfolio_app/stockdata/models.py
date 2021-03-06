from django.db import models


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    ticker = models.CharField(max_length=3)
    industry = models.CharField(max_length=30)
    rating = models.CharField(max_length=4, default='NONE')
    index = models.CharField(max_length=30)
    summary = models.TextField(default='additional info about company')

    def __str__(self):
        return self.name


class Index(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)



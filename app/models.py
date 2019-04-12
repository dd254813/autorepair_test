from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    car = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Schedule(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    #time = models.TimeField(auto_now=False, null=True)
    time_m = models.CharField(max_length=5)

    def __unicode__(self):
        return self.worker.name

    def __str__(self):
        return self.worker.name

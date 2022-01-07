from django.db import models


class Btc(models.Model):
    id = models.AutoField(primary_key=True)
    private_key = models.CharField(max_length=500)
    public_key = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

    objects = models.Manager()

    def __str__(self):
        return self.address



class Eth(models.Model):
    id = models.AutoField(primary_key=True)
    private_key = models.CharField(max_length=500)
    public_key = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

    objects = models.Manager()

    def __str__(self):
        return self.address




from django.db import models

# Create your models here.


class Workers(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fio = models.CharField(max_length=70)
    image = models.ImageField()
    passport_seria = models.CharField(max_length=10)
    direction = models.CharField(max_length=40)
    came_in = models.DateTimeField(auto_now_add=True,editable=False)
    cabinet = models.IntegerField(unique=True)
    date_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    passport_image = models.FileField()
    gender = models.CharField(max_length=10)
    live_place_now = models.CharField(max_length=100)
    university_finished_in = models.DateField()
    university_finished_sertificate = models.FileField()
    update_at = models.DateTimeField(auto_now=True, editable=False)
    howmany_patient = models.IntegerField()

    def __str__(self):
        return self.fio


class Clients(models.Model):
    fio = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=20)
    direction = models.CharField(max_length=40)
    will_come = models.DateTimeField()
    qr_code = models.ImageField()
    gender = models.CharField(max_length=10)
    date_birth = models.DateField()
    is_came = models.BooleanField()

    def __str__(self):
        return self.qr_code


class Arxiv(models.Model):
    clients = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
    complaint = models.CharField(max_length=500)
    rate = models.IntegerField()
    conclusion = models.CharField(max_length=500)
    reciepe = models.CharField(max_length=500)
    by_whom = models.CharField(max_length=500)

    def __str__(self):
        return self.complaint






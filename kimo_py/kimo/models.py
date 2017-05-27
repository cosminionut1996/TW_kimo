from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class Utilizator(AbstractBaseUser):
    """This model will store information about all the workers."""
    id = models.IntegerField(primary_key=True)
    nume = models.CharField(max_length=26)
    prenume = models.CharField(max_length=26)
    subscriptie = models.CharField(max_length=26)
    adresa = models.CharField(max_length=128)
    localitate = models.CharField(max_length=20)
    telefon = models.CharField(max_length=26)
    username = models.CharField(max_length=26)
    parola = models.CharField(max_length=26)
    expirare = models.DateField()

    USERNAME_FIELD = 'username'
    PASSWORD_FIELD = 'parola'
    REQUIRED_FIELDS = (username, parola)

    class Meta:
        db_table = "UTILIZATOR"


class Copil(models.Model):
    id=models.IntegerField(primary_key=True)
    nume = models.CharField(max_length=26)
    prenume = models.CharField(max_length=26)
    coliziuni_obiecte=models.IntegerField()
    izbituri_sol=models.IntegerField()
    contact_animale=models.IntegerField()


    class Meta:
        db_table= 'COPIL'

class Device(models.Model):
    id=models.IntegerField(primary_key=True)
    id_copil=models.IntegerField()
    longitudine=models.FloatField()
    latitudine=models.FloatField()

    class Meta:
        db_table= 'DEVICE'

class Legatura(models.Model):
    id_parinte=models.IntegerField()
    id_copil=models.IntegerField()

    class Meta:
        db_table= 'LEGATURA'

class Zona_Aprobata:
    id = models.IntegerField(primary_key=True)
    id_parinte = models.IntegerField()
    id_copil = models.IntegerField()
    longitudine1 = models.FloatField()
    latitudine1 = models.FloatField()
    longitudine2 = models.FloatField()
    latitudine2 = models.FloatField()
    denumire=models.CharField(max_length=30)
    descriere=models.CharField(max_length=100)

    class Meta:
        db_table= 'ZONA_APROBATA'

class Zona_Risc:
    id=models.IntegerField(primary_key=True)
    grad_pericol=models.IntegerField()
    tip_pericol=models.CharField(max_length=30)
    longitudine1 = models.FloatField()
    latitudine1 = models.FloatField()
    longitudine2 = models.FloatField()
    latitudine2 = models.FloatField()

    class Meta:
        db_table='ZONA_RISC'

class Notificari:
    id=models.IntegerField(primary_key=True)
    titlu=models.CharField(max_length=20)
    continut=models.CharField(max_length=100)
    ora=models.DateField()
    culoare=models.CharField(max_length=15)
    id_parinte=models.IntegerField()

    class Meta:
        db_table='NOTIFICARI'



from settings import SESSION_USER_ID_FIELD_NAME

from django.db import models


# Create your models here.
class Utilizator(models.Model):
    """This model will store information about all the workers."""
    id = models.IntegerField(primary_key=True)
    nume = models.CharField(max_length=26)
    prenume = models.CharField(max_length=26)
    subscriptie = models.CharField(max_length=26)
    adresa = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    localitate = models.CharField(max_length=20)
    telefon = models.CharField(max_length=26)
    username = models.CharField(max_length=26, unique=True)
    parola = models.CharField(max_length=26)
    expirare = models.DateField()

    class Meta:
        db_table = "UTILIZATOR"

    @classmethod
    def authenticate(cls, username, password):
        try:
            return cls.objects.get(username=username, parola=password)
        except Exception:
            return None

    def login(self, request):
        request.session[SESSION_USER_ID_FIELD_NAME] = self.id

    def logout(self, request):
        if request.session:
            del request.session


class Copil(models.Model):
    id = models.IntegerField(primary_key=True)
    nume = models.CharField(max_length=26)
    prenume = models.CharField(max_length=26)
    ultima_locatie=models.CharField(max_length=25)
    coliziuni_obiecte = models.IntegerField()
    izbituri_sol = models.IntegerField()
    contact_animale = models.IntegerField()

    class Meta:
        db_table = 'COPIL'


class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    id_copil = models.IntegerField()
    longitudine = models.FloatField()
    latitudine = models.FloatField()
    token = models.CharField(max_length=6)

    class Meta:
        db_table = 'DEVICE'


class Legatura(models.Model):
    id = models.IntegerField(primary_key=True)
    id_parinte = models.IntegerField()
    id_copil = models.IntegerField()

    class Meta:
        db_table = 'LEGATURA'



class ZonaAprobata(models.Model):
    id = models.IntegerField(primary_key=True)
    id_parinte = models.IntegerField()
    id_copil = models.IntegerField()
    longitudine1 = models.FloatField()
    latitudine1 = models.FloatField()
    longitudine2 = models.FloatField()
    latitudine2 = models.FloatField()
    denumire = models.CharField(max_length=30)
    descriere = models.CharField(max_length=100)

    class Meta:
        db_table = 'ZONA_APROBATA'


class ZonaRisc(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
    coordinates = models.CharField(max_length=1024)
    id_utilizator = models.IntegerField()

    class Meta:
        db_table = 'ZONA_RISC'


class Notificari(models.Model):
    id = models.IntegerField(primary_key=True)
    titlu = models.CharField(max_length=20)
    continut = models.CharField(max_length=100)
    ora = models.DateTimeField()
    culoare = models.CharField(max_length=15)
    id_parinte = models.IntegerField()

    class Meta:
        db_table = 'NOTIFICARI'

from django.db import models

class Film(models.Model):
    tytul = models.CharField(max_length=32)
    opis = models.TextField(max_length=256)
    po_premierze = models.BooleanField(default=False)
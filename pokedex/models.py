

from django.db import models
from django.db.models.functions.text import Length

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length = 30, null = False)

    POKEMON_TYPES = [
        ('A', 'Agua'),
        ('E', 'Electrico'),
        ('F', 'Fuego'),
        ('L', 'Lagartija'),
        ('P', 'Planta'),
        ('T', 'Tierra'),
    ]
    type = models.CharField(max_length = 30, null = False, choices = POKEMON_TYPES)
    weight = models.DecimalField(null = False, default = 1, max_digits= 4, decimal_places=2)
    height = models.DecimalField(null = False, default = 1, max_digits= 4, decimal_places=2)

    def __str__(self):
        return self.name

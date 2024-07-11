from django.contrib import admin
from .models import Pokemon

# Register your models here.

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'weight', 'height')

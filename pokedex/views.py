from django.http import HttpResponse
from django.template import loader

from pokedex.models import Pokemon

def index(request):
    pokemons = Pokemon.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon):
    template = loader.get_template('display_pokemon.html')
    pokemon = Pokemon.objects.get(name=pokemon)

    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

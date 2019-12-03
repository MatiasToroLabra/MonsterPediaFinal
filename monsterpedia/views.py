from django.shortcuts import render
from .models import Species, Armor, Monster
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):

    num_armor=Armor.objects.all().count()
    num_species=Species.objects.all().count()
    num_monster=Monster.objects.all().count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_armor':num_armor,'num_species':num_species,'num_monster':num_monster,'num_visits':num_visits},
    )

def login(request):

    num_armor=Armor.objects.all().count()
    num_species=Species.objects.all().count()
    num_monster=Monster.objects.all().count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'login2.html',
        context={'num_armor':num_armor,'num_species':num_species,'num_monster':num_monster,'num_visits':num_visits},
    )

def register(request):

    num_armor=Armor.objects.all().count()
    num_species=Species.objects.all().count()
    num_monster=Monster.objects.all().count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'register2.html',
        context={'num_armor':num_armor,'num_species':num_species,'num_monster':num_monster,'num_visits':num_visits},
    )

def registersmash(request):

    num_armor=Armor.objects.all().count()
    num_species=Species.objects.all().count()
    num_monster=Monster.objects.all().count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'registersmash.html',
        context={'num_armor':num_armor,'num_species':num_species,'num_monster':num_monster,'num_visits':num_visits},
    )

class MonsterListView(generic.ListView):
    model = Monster
    paginate_by = 10

class MonsterDetailView(generic.DetailView):
    model = Monster

class ArmorDetailView(generic.DetailView):
    model = Armor

class ArmorListView(generic.ListView):
    model = Armor
    paginate_by = 10

class ArmorCreate(CreateView):
    model = Armor
    fields = '__all__'

class ArmorUpdate(UpdateView):
    model =    Armor
    fields = '__all__'

class ArmorDelete(DeleteView):
    model = Armor
    success_url = reverse_lazy('armors')

from django.views import generic
class ArmorDetailView(generic.DetailView):
    model = Armor

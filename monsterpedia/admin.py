from django.contrib import admin

# Register your models here.

from . models import Species, Armor, Monster

admin.site.register(Species)
admin.site.register(Monster)
admin.site.register(Armor)

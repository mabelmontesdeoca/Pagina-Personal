from django.contrib import admin
from .models import Ciudad, Persona, Telefono, Email


# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Persona)
admin.site.register(Telefono)
admin.site.register(Email)

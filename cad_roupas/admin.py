from django.contrib import admin
from .models import VestidoNoiva
from .models import Cliente, VestidoFormatura, VestidoFesta, TernoNoivo, Smoking, Blazer

# Register your models here.
admin.site.register(VestidoNoiva)
admin.site.register(VestidoFormatura)
admin.site.register(VestidoFesta)
admin.site.register(TernoNoivo)
admin.site.register(Smoking)
admin.site.register(Blazer)

from django.contrib import admin
from .models import Clientes

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display= ("Usuario","Orden", "Phone", "Cantidad",)

admin.site.register(Clientes, ClientesAdmin)
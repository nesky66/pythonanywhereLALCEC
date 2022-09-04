from django.contrib import admin

# Register your models here.
from apps.usuarios.models import Usuario

class AdminUsuario(admin.ModelAdmin):
    list_display =   ('id','username','first_name','last_name',
                      'email','is_staff','is_active','is_superuser')

admin.site.register(Usuario,AdminUsuario)
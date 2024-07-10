from django.contrib import admin

from .models import Categoria, Vinilo, Rock, Clasica, Jazz

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Vinilo)
admin.site.register(Rock)
admin.site.register(Clasica)
admin.site.register(Jazz)


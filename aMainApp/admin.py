from django.contrib import admin
from .models import gelenMesajlar, makaleYaz
# Register your models here.



class messagesAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    list_display_links = ['name']
    
    class Meta:
        model = gelenMesajlar



class makaleAdmin(admin.ModelAdmin):
    list_display = ['yazi_ismi']
    list_filter = ['yazi_ismi']
    list_display_links = ['yazi_ismi']
    
    class Meta:
        model = makaleYaz
admin.site.register(makaleYaz, makaleAdmin)
admin.site.register(gelenMesajlar, messagesAdmin)
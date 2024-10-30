from django.contrib import admin
from .models import Comments , Messsages 
# Register your models here.

@admin.register(Comments)
class CommetnsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'user' , 'created_at')
    ordering = [ 'id' ,'created_at'] 
    list_editable = ('user' ,)
    search_fields = ['user__username']

     

admin.site.register(Messsages)
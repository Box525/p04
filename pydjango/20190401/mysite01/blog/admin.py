from django.contrib import admin
from blog.models import Auther

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('aname', 'asex', 'info')

admin.site.register(Auther,BlogAdmin)

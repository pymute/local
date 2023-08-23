from django.contrib import admin
from .models import News
from .forms import NewsForms

class Cloun(admin.ModelAdmin):
    fields = ('title','text')
    form = NewsForms


admin.site.register(News,Cloun)


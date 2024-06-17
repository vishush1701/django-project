from django.contrib import admin
from .models import Challenge

# Register your models here.
class BookAdmin(admin.ModelAdmin):
   readonly_fields = ("months_challenge",)
   prepopulated_fields ={"months_challenge":("month")}

admin.site.register(Challenge)

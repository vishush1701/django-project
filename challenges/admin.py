from django.contrib import admin
from .models import Challenge

# Register your models here.
class ChallengeAdmin(admin.ModelAdmin):
   readonly_fields = ("months_challenge",)
   list_display=("month","months_challenge",)
   list_filter = ("is_active",)

admin.site.register(Challenge,ChallengeAdmin)

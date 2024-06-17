from django.db import models

# Create your models here.
class Challenge(models.Model):
    month = models.CharField(max_length=10,null=False)
    challenge = models.CharField(max_length=25,null=False)
    is_active = models.BooleanField(default=False)
    managed = True

    def __str__(self) -> str:
        return f"month:{self.month} challenge:{self.challenge} is_active:{self.is_active}"

from django.db import models
from django.utils.text import slugify

# Create your models here.
class Challenge(models.Model):
    month = models.CharField(max_length=10,null=False)
    challenge = models.CharField(max_length=25,null=False)
    is_active = models.BooleanField(default=False)
    months_challenge = models.SlugField(max_length = 20,default="",editable=True,null=True)
    managed = True
    

    def save(self,*args, **kwargs):
        self.months_challenge = slugify(self.month)
        super().save(*args,**kwargs)

    def __str__(self) -> str:
        return f"month:{self.month} challenge:{self.challenge} is_active:{self.is_active} months_challenge={self.months_challenge}"

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class gelenMesajlar(models.Model):
    name = models.TextField(max_length=100)
    mail = models.TextField(max_length=200)
    telno = models.TextField(max_length=100)
    message = models.TextField(max_length=1000)
    

class makaleYaz(models.Model):
    image1 = models.ImageField(null=True, blank=True, upload_to="static/images")
    yazi_ismi = models.CharField(max_length=200, default="")
    yazi_onsoz = models.TextField(max_length=1000, default="")
    yazi = RichTextField(max_length=99999999999999, default="")
    slug = models.SlugField(default="", null=False, blank=True, editable=False)
    
    def save(self, *args, **kargs):
        self.slug = slugify(self.yazi_ismi)
        super().save(args, kargs)
    
from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Description = models.CharField(max_length=400)
    poster = models.ImageField(upload_to='poster')
    Thumbnail=models.ImageField(upload_to='poster')

    class Meta:
        ordering:('Title')

    def __str__(self):
        return self.Title

    def get_image(self):
        if self.poster:
            return 'http://127.0.0.1:8000'+ self.poster.url
        else:
            return ''
    
    def get_thumbnail(self):
        if self.Thumbnail:
            return 'http://127.0.0.1:8000' +self.Thumbnail.url
        else:
            if self.poster:
                self.Thumbnail= self.make_thumbnail(self.poster)
                self.save()
                return 'http://127.0.0.1:8000' +self.Thumbnail.url
            return ''
                

    def make_thumbnail(self, poster, size=(70,70)):
        img = Image.open(poster)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thum_io, 'JPEG', quality=85)

        thumbnail =File(thum_io, name=poster.name)

        return thumbnail

    

    

    

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thubmnail(output_size)
    #         img.save(self.image.path)

# Create your models here.


# class Pdfs(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     branch = models.CharField(max_length=100)
#     year = models.CharField(max_length=100)
#     sem = models.CharField(max_length=100)
#     pdf_name = models.CharField(max_length=100)
#     # op_price = models.CharField(max_length=100)
#     # sp_price = models.CharField(max_length=100)
#     date_posted = models.DateTimeField(default=timezone.now)
#     # book_img = models.ImageField(upload_to="pics")
#     # email = models.CharField(max_length=100)
#     # contact = models.CharField(max_length=100)
#     pdf_file = models.FileField(upload_to='pdfs')

#     def __str__(self):
#         return self.pdf_name

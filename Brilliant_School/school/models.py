from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=255, verbose_name="Notice Title")
    description = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")
    file = models.FileField(upload_to='notices/', blank=True, null=True, verbose_name="Attachment (PDF/Image)")

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

# Teacher Model
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='teachers/', blank=True, null=True)
    father_name = models.CharField(max_length=100, default="Unkown")
    mother_name = models.CharField(max_length=100, default="Unknown")
    date_of_birth = models.DateField(default="2000-01-01")
    religion = models.CharField(max_length=50, default="Islam")
    gender = models.CharField(max_length=10, default="Other")
    blood_group = models.CharField(max_length=5, default='N/A')
    education_qualification = models.TextField(default="Not specified")
    gmail = models.EmailField(default="example@gmail.com")
    mobile = models.CharField(max_length=15, default="01000000000")
    address = models.TextField(default="Not provided")

    def __str__(self):
        return self.name


# Notice Model
class Notice(models.Model):
    title = models.CharField(max_length=255, verbose_name="Notice Title")
    description = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")
    file = models.FileField(upload_to='notices/', blank=True, null=True, verbose_name="Attachment (PDF/Image)")

    def __str__(self):
        return self.title


# Student Model
CLASS_CHOICES = [
    ('প্লে', 'প্লে'),
    ('নার্সারি', 'নার্সারি'),
    ('প্রথম', 'প্রথম'),
    ('দ্বিতীয়', 'দ্বিতীয়'),
    ('তৃতীয়', 'তৃতীয়'),
    ('চতুর্থ', 'চতুর্থ'),
    ('পঞ্চম', 'পঞ্চম'),
    ('ষষ্ঠ', 'ষষ্ঠ'),
    ('সপ্তম', 'সপ্তম'),
    ('অষ্টম', 'অষ্টম'),
    ('নবম', 'নবম'),
    ('দশম', 'দশম'),
]

class Student(models.Model):
  name = models.CharField(max_length=100, verbose_name="নাম", default="অজানা")
  father_name = models.CharField(max_length=100, verbose_name="পিতার নাম", default="অজানা")
  mother_name = models.CharField(max_length=100, verbose_name="মাতার নাম", default="অজানা")
  mobile_number = models.CharField(max_length=15, verbose_name="মোবাইল নম্বর", default="০১৭XXXXXXXX")
  student_class = models.CharField(max_length=50, choices=CLASS_CHOICES, verbose_name="শ্রেণি", default="প্লে")
  date_of_birth = models.DateField(verbose_name="জন্ম তারিখ", default="2000-01-01")
  blood_group = models.CharField(max_length=5, default='N/A', verbose_name="রক্তের গ্রুপ")
  religion = models.CharField(max_length=50, default="ইসলাম", verbose_name="ধর্ম")
  address = models.TextField(verbose_name="ঠিকানা", default="গ্রাম, উপজেলা, জেলা")

  def __str__(self):
        return self.name

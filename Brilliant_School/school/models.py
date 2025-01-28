from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Teacher Model
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, default='Teacher')
    profile_pic = models.ImageField(upload_to='teachers/', blank=True, null=True)
    father_name = models.CharField(max_length=100, default="Unkown")
    mother_name = models.CharField(max_length=100, default="Unknown")
    date_of_birth = models.DateField(default="1985-01-01")
    religion = models.CharField(max_length=50, default="Islam")
    gender = models.CharField(max_length=10, default="N/A")
    blood_group = models.CharField(max_length=5, default='N/A')
    education_qualification = models.TextField(default="Not specified")
    gmail = models.EmailField(default="example@gmail.com")
    mobile = models.CharField(max_length=15, default="01xxxxxxxxx")
    address = models.TextField(default="পাবনা")
    hobby = models.CharField(max_length=200, default="Not specified") 
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
SECTION_CHOICES = [
    ('ক', 'ক'),
    ('খ', 'খ'),
    ('গ', 'গ'),
    ('বিজ্ঞান', 'বিজ্ঞান'),
    ('বানিজ্য', 'বানিজ্য'),
    ('মানবিক', 'মানবিক'),
    ('None', 'No Section'),   
]

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="নাম", default="অজানা")
    father_name = models.CharField(max_length=100, verbose_name="পিতার নাম", default="অজানা")
    mother_name = models.CharField(max_length=100, verbose_name="মাতার নাম", default="অজানা")
    mobile_number = models.CharField(max_length=15, verbose_name="মোবাইল নম্বর", default="N/A")
    student_class = models.CharField(max_length=50, choices=CLASS_CHOICES, verbose_name="শ্রেণি", default="N/A")
    section = models.CharField(max_length=50, choices=SECTION_CHOICES, verbose_name="শাখা", default="None")
    roll_number = models.PositiveIntegerField(verbose_name="রোল নম্বর")
    date_of_birth = models.DateField(verbose_name="জন্ম তারিখ", default="2010-01-01")
    blood_group = models.CharField(max_length=5, default='N/A', verbose_name="রক্তের গ্রুপ")
    religion = models.CharField(max_length=50, default="N/A", verbose_name="ধর্ম")
    address = models.TextField(verbose_name="ঠিকানা", default="N/A")

    class Meta:
        unique_together = ('student_class', 'section', 'roll_number')

    def clean(self):
        """Validate uniqueness before saving."""
        if Student.objects.filter(
            student_class=self.student_class, 
            section=self.section, 
            roll_number=self.roll_number
        ).exclude(pk=self.pk).exists():
            raise ValidationError(
                f"Roll number {self.roll_number} already exists in class {self.student_class} section {self.section}."
            )

    def save(self, *args, **kwargs):
        self.full_clean()  # Ensure `clean()` runs before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} (Class: {self.student_class}, Section: {self.section}, Roll: {self.roll_number})"
    
class Attendance(models.Model):
    date = models.DateField(verbose_name="তারিখ", auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="শিক্ষার্থী")
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')],
        verbose_name="স্থিতি"
    )

    def __str__(self):
        return f"{self.student.name} ({self.student.student_class}-{self.student.section}) - {self.date} - {self.status}"
    



class SMSMessage(models.Model):
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Sent', 'Sent'), ('Failed', 'Failed')])

    def __str__(self):
        return f"SMS to {self.phone_number}"

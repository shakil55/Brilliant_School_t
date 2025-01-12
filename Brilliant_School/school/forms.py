from django import forms
from .models import Student, Teacher, Notice

class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)

    class Meta:
        model = Student
        fields = [
            'name', 
            'father_name', 
            'mother_name', 
            'mobile_number', 
            'student_class', 
            'date_of_birth', 
            'blood_group', 
            'religion', 
            'address'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'নাম লিখুন'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'বাবার নাম'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'মায়ের নাম'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'মোবাইল নম্বর'}),
            'student_class': forms.Select(attrs={'class': 'form-control'}),
            'blood_group': forms.TextInput(attrs={'class': 'form-control'}),
            'religion': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ঠিকানা লিখুন'}),
        }

class TeacherForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)

    class Meta:
        model = Teacher
        fields = [
            'name', 
            'father_name', 
            'mother_name', 
            'date_of_birth', 
            'religion', 
            'gender', 
            'blood_group', 
            'education_qualification', 
            'gmail', 
            'mobile', 
            'address'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'নাম লিখুন'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'বাবার নাম'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'মায়ের নাম'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'religion': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'blood_group': forms.TextInput(attrs={'class': 'form-control'}),
            'education_qualification': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gmail': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ঠিকানা লিখুন'}),
        }

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'নোটিশের শিরোনাম'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'নোটিশের বিবরণ'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

from django.db import models

# Create your models here.

class Common_Teacher_Student(models.Model):
    gen = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    idno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    subject = models.CharField(max_length=50)
    contact_no = models.IntegerField(unique=True)
    gender = models.CharField(max_length=10,choices=gen)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=100,unique=True)

    class Meta:
        abstract = True


class Teacher(Common_Teacher_Student):
    date_of_join = models.DateField()
    salary = models.IntegerField()
    photo = models.ImageField(upload_to="Teacher_Images/")


class Student(Common_Teacher_Student):
    marks = models.IntegerField()
    photo = models.ImageField(upload_to="Student_Images/")





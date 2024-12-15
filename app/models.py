from django.db import models

class Crypto(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=256)

    def __str__(self):
        return self.author


class School(models.Model):
    class InstitutionType(models.Choices):
        PRIVATE = 'PR' 'Частная'
        PUBLIC = 'PB' 'Государственная'
    
    class Status(models.Choices):
        GYMNASIUM = 'GM' 'Гимназия'
        LYCEUM = 'LC' 'Лицей'
        GENERAL_EDUCATION = 'GE' 'Общеобразовательная'
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    institution_type = models.CharField(max_length=255, choices=InstitutionType)
    status = models.CharField(max_length=255, choices=Status)

    def __str__(self):
        return f'{self.name} ({self.status}) – {self.institution_type}'


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    student_class = models.CharField(max_length=3)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_class})"

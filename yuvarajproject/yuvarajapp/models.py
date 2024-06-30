from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/', null=True, blank=True)

    def __str__(self):
        return self.name

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    language1 = models.DecimalField(max_digits=5, decimal_places=2)
    language2 = models.DecimalField(max_digits=5, decimal_places=2)
    acting = models.DecimalField(max_digits=5, decimal_places=2)
    dance = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.name}'s Marks"

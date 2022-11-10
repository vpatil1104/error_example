from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    assignment_assign = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.emp_id
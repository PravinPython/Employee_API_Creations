from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
def validate_names(value):
    if type(value) == str and len(value) >= 5:
        return value
    else:
        raise ValidationError("Invalid Name..!")


def validate_emails(value):
    if type(value) == str and len(value) >= 11 and "@gmail.com":  # s@ab.in
        return value
    else:
        raise ValidationError("Invalid Name..!")


class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=30, default='Guest')
    phone_num = models.BigIntegerField(unique=True)
    joiningDate = models.DateField()
    address = models.CharField(max_length=255, default='Y')

    class Meta:
        db_table = 'EMPLOYEE_MASTER'
        ordering = ['role']  # select * from employee_master order by role desc

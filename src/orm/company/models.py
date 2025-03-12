from django.db import models


# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField(null=True)
    department = models.ForeignKey(
        "company.Department",
        related_name="employees",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.fullname} - {self.post}. Department: {self.department}"


class Department(models.Model):
    fullname = models.CharField(max_length=255)
    floor = models.SmallIntegerField()
    branch_office = models.ForeignKey(
        "company.BranchOffice",
        related_name="departments",
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.fullname}"


class BranchOffice(models.Model):
    address = models.CharField(max_length=255)
    shortname = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.shortname} on {self.address}"

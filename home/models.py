from django.db import models

# Create your models here.
class homes(models.Model):
    expenseName = models.TextField(default="abc",max_length=30)
    expenseAmount = models.IntegerField(default="0000000")
    date = models.DateField(null=True)

    def __str__(self):
        return self.expenseName
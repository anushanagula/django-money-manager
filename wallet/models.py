from django.db import models


from django.contrib.auth.models import User

class Income(models.Model):
    amount = models.IntegerField()
    category = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=True, blank=True)
    note = models.CharField(blank=True,max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.category
class Expense(models.Model):
    amount = models.IntegerField()
    category = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=True, blank=True)
    note = models.CharField(blank=True,max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.category
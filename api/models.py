from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WorkDay(models.Model):
    choices = (
        ('monday','monday'),
        ('tuesday','tuesday'),
        ('wednesday','wednesday'),
        ('thursday','thursday'),
        ('friday','friday'),
        ('saturday','saturday'),
        ('sunday','sunday'),
    )
    day = models.CharField(max_length=20, blank=True, null=True, choices=choices)
    check_in_time = models.TimeField(auto_now=False, auto_now_add=False)
    departure_time = models.TimeField(auto_now=False, auto_now_add=False)

class WorkingHours(models.Model):
    workday = models.ManyToManyField(WorkDay, blank = True)

class Browser(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=20)
    os = models.CharField(max_length=20)

class Mark(models.Model):
    employee       = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    place          = models.CharField(max_length=99)
    check_in_time  = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField(null=True, blank=True)
    browser        = models.ForeignKey(Browser, on_delete = models.CASCADE)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    choices = (
        ('employee','employee'),
        ('manager','manager'),
    )

    def path(self, filename):
        return f'account/{self.user.username}/avatar/{filename}'

    avatar = models.ImageField(upload_to = path, null = True, blank = True)
    role = models.CharField(max_length=20, blank=True, null=True, choices=choices)
    working_hours = models.ForeignKey(WorkingHours, on_delete = models.CASCADE, blank=True, null=True)
    marks = models.ManyToManyField(Mark, blank = True)

class Business(models.Model):
    name            = models.CharField(max_length=99, blank=True, null=True)
    employees       = models.ManyToManyField(Account, blank = True)
    marks           = models.ManyToManyField(Mark, blank = True)
    external_system = models.BooleanField(default=False)
    redirect_to     = models.CharField(max_length=999, blank=True, null=True)
    us              = models.TextField(default='', blank=True, null=True)

    def path(self, filename):
        return f'business/{self.name}/image/{filename}'

    image = models.ImageField(upload_to = path, null = True, blank = True)
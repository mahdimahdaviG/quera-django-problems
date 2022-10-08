from django.db import models
from django_jalali.db.models import jDateField, jDateTimeField
import jdatetime

GENDER_CHOICES = (
    ("M", "MALE"),
    ("F", "FEMALE"),
)

class CustomUser(models.Model):
    username = models.CharField(max_length=256, default='')
    full_name = models.CharField(max_length=256, default='')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, default='')
    national_code = models.CharField(max_length=10, default='')
    birthday_date = jDateField()
    ceremony_datetime = jDateTimeField()
    country = models.CharField(default="Iran", max_length=4)

    def get_first_and_last_name(self):
        name = self.full_name.split()
        self.first_name = name[0]
        self.last_name = name[1]

        return {'first_name': self.first_name, 'last_name': self.last_name}
    
    def get_age(self):
        age = jdatetime.date.today() - self.birthday_date
        
        return age.days // 365

    def is_birthday(self):
        month = self.birthday_date.month
        day = self.birthday_date.day

        return (month == jdatetime.date.today().month and day == jdatetime.date.today().day)

class Birthday(models.Model):
    pass

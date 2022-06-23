from django.db import models

# Create your models here.

class Insurance(models.Model):

    class Company(models.TextChoices):
        JORDANCARE = ('JordanCare')
        SAURON_HEALTH = ('Sauron_Health')
        DELAY_THE_INEVITABLE = ('Delay The Inevitable')
        FLORIDA_GUNS_AND_MEDICINE = ('Florida Guns & Medicine')
        SITHCARE = ('SithCare')
        WAFFLE_HOUSE = ('Waffle House')
        FOR_RICH_PEOPLE_ONLY = ('For Rich People Only')

    company = models.CharField(
        max_length=50,
        choices = Company.choices,
        default = Company.JORDANCARE
        )
    accountHolder = models.CharField(max_length=32)
    policyNumber = models.IntegerField()
    idNumber = models.IntegerField()

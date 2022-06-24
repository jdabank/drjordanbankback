from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Appointment(models.Model):

    class Reason(models.TextChoices):
        PLASTIC_SURGERY = ('Plastic Surgery')
        NECROMANCY = ('Necromancy')
        ALLERGIES = ('Allergies')
        JERUSALEM_SYNDROME = ('Jerusalem Syndrome')
        ATE_TOO_MUCH = ('Ate too much')

    class Physician(models.TextChoices):
        JORDAN_BANK = ('Jordan Bank')
        MEILING_LI = ('Meiling Li')
        TYGER_SALTERS = ('Tyger Salters')
        OFORI_MANSON = ('Ofori Manson')
        KEVIN_HA = ('Kevin Ha')
        JEAN_ENG = ('Jean Eng')
        RAFAY_HASSAN = ('Rafay Hassan')

    physician = models.CharField(
        max_length=50,
        choices = Physician.choices,
        default = Physician.JORDAN_BANK
        )
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    reason = models.CharField(
        max_length=50,
        choices = Reason.choices,
        default = Reason.PLASTIC_SURGERY
        )
    details = models.CharField(max_length=500)

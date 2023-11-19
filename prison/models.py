from django.db import models
from . timemodel import TimeModel



class Prisoner(TimeModel):
    GENDER = (
        ("MALE", "Male"),
        ("FEMALE", "Female")
    )
    f_name = models.CharField(("First Name"), max_length=15)
    l_name = models.CharField(("Last Name"), max_length=15)
    gender = models.CharField(choices=GENDER, max_length=50)
    dob = models.DateField(("Date of Birth"), auto_now=False, auto_now_add=False)
    blood_tp = models.CharField(("Blood Type"), max_length=50, blank=True)
    offense_type = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    state = models.CharField(max_length=50)
    nationality = models.CharField(default="Nigeria" ,max_length=50)
    tribe = models.CharField(max_length=50)
    img = models.ImageField(("Passport"), upload_to="prisoner/images", height_field=None, width_field=None, max_length=None)
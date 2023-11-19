from django.db import models
from . timemodel import TimeModel


class Prisoner(TimeModel):
    f_name = models.CharField(("First Name"), max_length=15)
    l_name = models.CharField(("Last Name"), max_length=15)
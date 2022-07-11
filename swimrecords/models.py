from django.db import models
from django.core.validators import *
from .validator import *


class SwimRecord(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    team_name = models.CharField(max_length=100, null=False)
    relay = models.BooleanField(null=False)
    stroke = models.CharField(max_length=100, null=False, validators=[validate_stroke])
    distance = models.IntegerField(validators=[validate_distance])
    record_date = models.DateTimeField(validators=[validate_record_date])
    record_broken_date = models.DateTimeField()


    def clean(self):
        super().clean()
        if self.record_broken_date and self.record_date and self.record_broken_date < self.record_date:
            raise ValidationError({"record_broken_date": "Can't break record before record was set."})
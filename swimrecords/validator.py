from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as text # import gettext_lazy
from django.utils import timezone
import re

def validate_stroke(stroke_type):
    valid_stroke_types = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke_type not in valid_stroke_types:
        raise ValidationError(text(f"{stroke_type} is not a valid stroke"))

def validate_distance(distance_value):
    if distance_value < 50:
        raise ValidationError(text("Ensure this value is greater than or equal to 50."))

def validate_record_date(record_date):
    if record_date > timezone.now():
        raise ValidationError(text("Can't set record in the future."))


        

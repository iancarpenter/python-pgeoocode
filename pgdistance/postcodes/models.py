from django.db import models

MEASUREMENT_UNITS = [
    ('KM', 'km'),
    ('M', 'miles'),
] 

class Postcode(models.Model):
    start_postcode = models.CharField(max_length=4)
    end_postcode = models.CharField(max_length=4)
    distance_unit = models.CharField(choices=MEASUREMENT_UNITS, max_length=22)
    #measurement_choice = forms.ChoiceField(label='Distance in Kilometers or Miles', widget=forms.RadioSelect(choices=MEASUREMENT_UNITS))



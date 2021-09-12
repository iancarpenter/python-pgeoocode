from django.shortcuts import render
from django.forms import modelform_factory
from .models import Postcode
import pgeocode


PostcodesForm = modelform_factory(Postcode, exclude=[])

def postcodes(request):
    if request.method == "POST":
        form = PostcodesForm(request.POST)
        if form.is_valid():
            form.save()
            
            start_postcode = form['start_postcode'].value()
            end_postcode = form['end_postcode'].value()

            dist = pgeocode.GeoDistance('GB')
            distance_result = dist.query_postal_code(start_postcode, end_postcode)
            measurement_unit = 'km'

            # convert to miles if 
            if form['distance_unit'].value() == 'M':
                distance_result = distance_result / 1.609 
                measurement_unit = 'miles'

            distance_result = round(distance_result,2)
            
            return render(request, "postcodes/postcodes.html", {"form": form, "distance_result":distance_result, 'measurement_unit': measurement_unit})

    else:
        form = PostcodesForm
        return render(request, "postcodes/postcodes.html", {"form": form})

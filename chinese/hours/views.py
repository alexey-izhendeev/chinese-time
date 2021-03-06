from django.shortcuts import render, get_object_or_404
from .calculations import solartime, positioner, find_hours, solar_to_chinese, chinese_time, me, now_time
import ephem
from django import forms


class TimeCalculator(forms.Form):
    lat = forms.DecimalField(max_digits=30, decimal_places=18, label='Latitude')
    long = forms.DecimalField(max_digits=30, decimal_places=18, label='Longitude')


def result_page(request):
    return render(request, 'hours/page/result_page.html', {'chin': chin, 'tim': tim, 'now': now, 'solar': solar})


def coordinates(request):
    if request.method == 'POST':
        form = TimeCalculator(request.POST)
        if form.is_valid():
            pos = ephem.Observer()  # ephem object
            pos.lat = str(form.cleaned_data['lat'])  # latitude
            pos.long = str(form.cleaned_data['long'])  # longitude
            solar = solartime(pos)  # solartime
            chin = solar_to_chinese(solartime(pos))  # chinese time
            tim = positioner(str(form.cleaned_data['lat']), str(form.cleaned_data['long']))  # position of user
            now = now_time  # ordinary time at user location
            return render(request, 'hours/page/result_page.html', {'chin': chin, 'tim': tim, 'now': now, 'solar': solar})

        else:
            return render(request, 'hours/page/coordinates.html', {
                'form': form
            })
    return render(request, 'hours/page/coordinates.html', {
        'form': TimeCalculator()
    })

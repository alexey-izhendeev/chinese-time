from django.shortcuts import render, get_object_or_404
from .ideas import solartime, positioner, find_hours, solar_to_chinese, chinese_time, me, now_time


def functional_page(request):
    chin = solar_to_chinese(solartime(me))
    tim = positioner()
    now = now_time
    return render(request, 'hours/page/func_page.html', {'chin': chin, 'tim': tim, 'now': now})




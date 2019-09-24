from django.shortcuts import render
from django.http import HttpResponse
from semaphore import rpi_methods as rpi


def index(request):
    lamp1 = request.GET.get("lamp1", None)
    lamp2 = request.GET.get("lamp2", None)
    lamp3 = request.GET.get("lamp3", None)

    if lamp1:
        rpi.toggle_led(1)
    elif lamp2:
        rpi.toggle_led(2)
    elif lamp3:
        rpi.toggle_led(3)

    context = {
        "lamp1": rpi.get_lamp_status(1),
        "lamp2": rpi.get_lamp_status(2),
        "lamp3": rpi.get_lamp_status(3),
    }

    return render(request, 'semaphore/index.html', context)

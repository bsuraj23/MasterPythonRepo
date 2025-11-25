from django.shortcuts import render
from django.http import HttpResponse
from .models import Ping


def ping_view(request):
    # create a Ping to demonstrate model/save -> signal
    p = Ping.objects.create(name='ping')
    return render(request, 'middleware_signals/ping.html', {'ping': p})


def header_echo(request):
    # simple raw response that shows middleware header
    resp = HttpResponse('Headers echoed')
    return resp

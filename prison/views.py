from django.shortcuts import render, request
from django.http import Http404
from .models import Prisoner, Onbail, Oncourt
# from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView



def prisonerList(request):
    prisoner = Prisoner.objects.all()
    return render(request, "prisoner/list.html", {
        'prisoner':prisoner
    })



def prisonerDetail(request, prisoner_id):
    try:
        prisoner = Prisoner.objects.get(pk=prisoner_id)
    except Prisoner.DoesNotExist:
        raise Http404("Prisoner doesn't exist")
    return render(request, "prisoner/detail.html", {
        'prisoner':prisoner
    })


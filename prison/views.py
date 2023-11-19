from django.shortcuts import render
from .models import Prisoner, Onbail, Oncourt
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView






class PrisonerCreateView(CreateView):
    model = Prisoner
    fields = "__all__"
    template_name = "prisoner/create.html"
    success_url = "list"
    





class PrisonerListView(ListView):
    model = Prisoner
    template_name = "prisoner/list.html"
    context_object_name = "prisoners"




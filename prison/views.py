from django.shortcuts import render, redirect
from django.http import Http404
from .models import Prisoner, Onbail, Oncourt
from django.shortcuts import get_object_or_404
from . forms import PrisonerUpdateForm, PrisonerCreateForm




def dashboard(request):
    prisoner = Prisoner.objects.all()
    return render(request, 'prisoner/dashboard.html', {
        'prisoner':prisoner
    })


# Prisoner list views
def prisonerList(request):
    prisoner = Prisoner.objects.all()
    return render(request, "prisoner/list.html", {
        'prisoner':prisoner
    })


# Prisoner Detail Views
def prisonerDetail(request, prisoner_slug):
    """
    Don't bother i just used this way `Http404`, insited of `get_object_or_404`
    """
    try:
        prisoner = Prisoner.objects.get(slug=prisoner_slug)
    except Prisoner.DoesNotExist:
        raise Http404("Prisoner doesn't exist")
    return render(request, "prisoner/detail.html", {
        'prisoner':prisoner
    })


# Prisoner Update views
def prisonerUpdate(request, prisoner_slug):
    prisoner = get_object_or_404(Prisoner, slug=prisoner_slug)
    form = PrisonerUpdateForm(instance=prisoner)
    if request.method =='POST':
        form = PrisonerUpdateForm(request.POST, instance=prisoner)
        if form.is_valid():
            form.save()
    return redirect('prisoner-list')


# Prisoner Create Views
def prisonerCreateView(request):
    if request.method == "POST":
        form = PrisonerCreateForm(request.POST)
        if form.is_valid():
            prisoner = form.save()
            return redirect("prisoner-deatil", slug=prisoner.slug)
    else:
        form = prisonerCreateView()
    return render(request, "prisoner_create.html", {
        "form":form,
        "edit_mode":False
    })


    # form = Prisoner(request.POST or None)
    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()
    #         return redirect("dashboard")
    
    # return render(request, 'prisoner', {
    #     "form":form
    # })
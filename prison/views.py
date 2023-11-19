from django.shortcuts import render, redirect
from django.http import Http404
from .models import Prisoner, Onbail, Oncourt
from django.shortcuts import get_object_or_404
from . forms import PrisonerUpdateForm



def dashboard(request):
    pass


# Prisoner list views
def prisonerList(request):
    prisoner = Prisoner.objects.all()
    return render(request, "prisoner/list.html", {
        'prisoner':prisoner
    })



# Prisoner Detail Views
def prisonerDetail(request, prisoner_id):
    """
    Don't bother i just used this way `Http404`, insited of `get_object_or_404`
    """
    try:
        prisoner = Prisoner.objects.get(pk=prisoner_id)
    except Prisoner.DoesNotExist:
        raise Http404("Prisoner doesn't exist")
    return render(request, "prisoner/detail.html", {
        'prisoner':prisoner
    })


# Prisoner Update views
def prisonerUpdate(request, prisoner_id):
    prisoner = get_object_or_404(Prisoner, id=prisoner_id)
    form = PrisonerUpdateForm(instance=prisoner)
    if request.method =='POST':
        form = PrisonerUpdateForm(request.POST, instance=prisoner)
        if form.is_valid():
            form.save()
    return redirect('prisoner-list')



# Prisoner Create Views
def prisonerCreateView(request):
    form = Prisoner(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    
    return render(request, 'prisoner', {
        "form":form
    })
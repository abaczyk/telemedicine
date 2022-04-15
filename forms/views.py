from django.shortcuts import render, redirect
from .forms import GeneralForm, PatientForm, DoctorForm, AllGroupsForm, Main


def main(request):
    if request.method == 'POST':
        form = Main(request.POST)
    form = Main()
    return render(request, 'main.html', {'form': form})

def general(request):
    if request.method == 'POST':
        form = GeneralForm(request.POST)
        if form.is_valid():
            if request.POST.get('whoIsRespondent') == 'Pacjent':
                return redirect('patient')
            else:
                return redirect('doctor')

    else:
        form = GeneralForm()

    return render(request, 'forms.html', {'form': form})


def patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            return redirect('allGroups') #TODO naprawic
    context = {}
    context['form'] = PatientForm()


    return render(request, 'forms.html', context)


def doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            return redirect('allGroups')

    else:
        form = DoctorForm()
    return render(request, 'forms.html', {'form': form})


def allGroups(request):
    context = {'form' : AllGroupsForm()}
    if request.method == 'POST':
        form = AllGroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankYou')
    return render(request, 'forms.html', context)

def thankYou(request):
    return render(request, 'thankYou.html')
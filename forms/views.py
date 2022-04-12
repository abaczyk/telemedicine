from django.shortcuts import render
from .forms import GeneralForm, PatientForm, DoctorForm, AllGroupsForm, Main


def main(request):

    if request.method == 'POST':
        form = Main(request.POST)
    form = Main()
    return render(request, 'forms.html', {'form': form})

def general(request):

    if request.method == 'POST':
        form = GeneralForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            residence = form.cleaned_data['residence']
            whoIsRespondent = form.cleaned_data['whoIsRespondent']
    else:
        form = GeneralForm()

    return render(request, 'forms.html', {'form': form})


def patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #
    else:
        form = PatientForm()

    return render(request, 'forms.html', {'form': form})

def doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #
    else:
        form = DoctorForm()

    return render(request, 'forms.html', {'form': form})


def allGroups(request):
    if request.method == 'POST':
        form = AllGroupsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AllGroupsForm()

    return render(request, 'forms.html', {'form': form})
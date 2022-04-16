from django.shortcuts import render, redirect
from .forms import GeneralForm, PatientForm, DoctorForm, AllGroupsForm
from .models import Patient, General, Doctor


def main(request):
    return render(request, 'main.html')

def general(request):
    context = {'form': GeneralForm()}
    if request.method == 'POST':
        form = GeneralForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get('whoIsRespondent') == 'Pacjent':
                instance = Patient()
                instance.respondentID = request.POST.get(id(request))
                return redirect('patient')
            else:
                instance = Doctor()
                instance.respondentID = request.POST.get('id')
                return redirect('doctor')
    return render(request, 'forms.html', context)


def patient(request):
    context = {'form': PatientForm()}
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allGroups') #TODO naprawic
    return render(request, 'forms.html', context)


def doctor(request):
    context = {'form': DoctorForm()}
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allGroups')
    return render(request, 'forms.html', context)


# def allGroups(request):
#     context = {'form': AllGroupsForm()}
#     if request.method == 'POST':
#         form = AllGroupsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('thankYou')
#     return render(request, 'forms.html', context)


def allGroups(request):
    context = {'form': DoctorForm()}
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankYou')
    return render(request, 'forms.html', context)

def thankYou(request):
    return render(request, 'thankYou.html')
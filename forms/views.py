from django.shortcuts import render, redirect
from .forms import GeneralForm, PatientForm, DoctorForm, AllGroupsForm
from .models import General, Doctor, Patient


def main(request):
    return render(request, 'main.html')

def general(request):
    context = {'form': GeneralForm()}
    if request.method == 'POST':
        form = GeneralForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get('whoIsRespondent') == 'Pacjent':
                return redirect('patient')
            else:
                return redirect('doctor')
        else:
            form = GeneralForm()
    return render(request, 'forms.html', context)


def patient(request):
    context = {'form': PatientForm()}
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allGroups') #TODO naprawic
        else:
            form = PatientForm()
    return render(request, 'forms.html', context)


def doctor(request, args=None):
    context = {'form': DoctorForm()}
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allGroups')
        else:
            form = DoctorForm()
    return render(request, 'forms.html', context)


def allGroups(request):
    context = {'form': AllGroupsForm()}
    if request.method == 'POST':
        form = AllGroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankYou')
        else:
            form = AllGroupsForm()
    return render(request, 'forms.html', context)


# def allGroups(request):
#     context = {'form': DoctorForm()}
#     if request.method == 'POST':
#         form = DoctorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('thankYou')
#     return render(request, 'forms.html', context)

def thankYou(request):
    return render(request, 'thankYou.html')
from datetime import datetime

from django.shortcuts import render, redirect

from .forms import GeneralForm, PatientForm, DoctorForm, AllGroupsForm
from .models import Patient, General, Doctor, AllGroups

sessionKey = None


def main(request):
    #close forms after 13.05.2022
    if str(datetime.now()) > "2022-05-13 00:00:00.0000":
        return render(request, 'closedForms.html')
    return render(request, 'main.html')


def getSession(request):
    request.session.create()
    sessionKey = request.session.session_key
    return sessionKey


def general(request):
    context = {'form': GeneralForm()}
    if request.method == 'POST':
        form = GeneralForm(request.POST)
        form.instance.sessionKey = getSession(request)
        context['form'] = form
        # obsługa cofania
        query_set = General.objects.filter(sessionKey=request.session.session_key)
        if query_set.exists():
            query_set[query_set.count() - 1].delete()
        if form.is_valid():
            form.save()
            # przekierowanie w zależności od osoby, która wypełniła ankietę
            if request.POST.get('whoIsRespondent') == 'Patient':
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
        form.instance.sessionKey = request.session.session_key
        form.instance.respondentID_id = General.objects.get(sessionKey=form.instance.sessionKey).id
        # obsługa cofania
        query_set = Patient.objects.filter(sessionKey=request.session.session_key)
        if query_set.exists():
            query_set[query_set.count() - 1].delete()
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('allGroups')
        else:
            form = PatientForm()
    return render(request, 'forms.html', context)


def doctor(request):
    context = {'form': DoctorForm()}
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        form.instance.sessionKey = request.session.session_key
        form.instance.respondentID_id = General.objects.get(sessionKey=form.instance.sessionKey).id
        # obsługa cofania
        query_set = Doctor.objects.filter(sessionKey=request.session.session_key)
        if query_set.exists():
            query_set[query_set.count() - 1].delete()
        context['form'] = form
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
        form.instance.sessionKey = request.session.session_key
        form.instance.respondentID_id = General.objects.get(sessionKey=form.instance.sessionKey).id
        # obsługa cofania
        query_set = AllGroups.objects.filter(sessionKey=request.session.session_key)
        if query_set.exists():
            query_set[query_set.count() - 1].delete()
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('thankYou')
        else:
            form = AllGroupsForm()
    return render(request, 'forms.html', context)


def thankYou(request):
    return render(request, 'thankYou.html')

"""Anna Baczyk 180849, Bartosz Czapla 181486
Plik zawierajacy przetwarzanie zadan"""

from datetime import datetime
from django.shortcuts import render, redirect
from .forms import GeneralForm, PatientForm, DoctorForm, AllGroupsForm
from .models import Patient, General, Doctor, AllGroups


# generowanie strony glownej
def main(request):
    if str(datetime.now()) > "2022-05-13 00:00:00.0000":  # zamknij ankiete po 12.05.2022
        return render(request, 'closedForms.html')
    return render(request, 'main.html')


# utworz klucz sesji
def getSession(request):
    request.session.create()
    sessionKey = request.session.session_key
    return sessionKey


# generowanie pytan ogolnych
def general(request):
    context = {'form': GeneralForm()}
    if request.method == 'POST':
        form = GeneralForm(request.POST)
        # tworzenie klucza sesji przy przeslaniu 1 strony ankiety
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


# generowanie pytan dla pacjenta
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


# generowanie pytan dla lekarza
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


# generowanie pytan koncowych
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


# generowanie podziekowania za wypelnienie ankiety
def thankYou(request):
    return render(request, 'thankYou.html')

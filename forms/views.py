"""Anna Baczyk 180849
Plik zawierajacy przetwarzanie zadan"""

from datetime import datetime
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from django.shortcuts import render, redirect
from .forms import GeneralForm, PatientForm, DoctorForm, AllGroupsForm
from .models import Patient, General, Doctor, AllGroups


def main(request):
    """Generowanie strony glownej"""
    if str(datetime.now()) > "2022-05-13 00:00:00.0000":  # zamknij ankiete po 12.05.2022
        return render(request, 'chooseResults.html')
    return render(request, 'main.html')


def statistics(request):
    """Wyswietlanie statystyk odnosnie danych"""
    df = pd.read_csv('static/all_data.csv')

    graphs = [get_graph(df, 'gender', 'Płeć:'), get_graph(df, 'age', 'Wiek'),
              get_graph(df, 'residence', 'Miejsce zamieszkania:'), get_graph(df, 'education', 'Wykształcenie:'),
              get_graph(df, 'employment', 'Status zatrudnienia:'),
              get_graph(df, 'purposeOfEConsultation', 'Cel teleporady:'),
              get_graph(df, 'whenWasEConsultation', 'Termin teleporady:'),
              get_graph(df, 'freqOfVisits', 'Częstość wizyt w POZ:'),
              get_graph(df, 'isProblemResolved', 'Czy problem został rozwiązany podczas teleporady?'),
              get_graph(df, 'wasVisitProposed', 'Czy została zaproponowana wizyta stacjonarna?'),
              get_graph(df, 'wereInstructionsClear', 'Czy instrukcje były jasne?'),
              get_graph(df, 'wasDoctorEngaged', 'Czy lekarz był zaangażowany?'),
              get_graph(df, 'eConsultationVsVisit', 'Teleporada czy wizyta stacjonarna?')]
    context = {'plot_div': graphs}
    return render(request, 'statistics.html', context=context)


def get_graph(df, name, title):
    """Utworzenie wykresow"""
    labels = df[name].value_counts().index
    values = df[name].value_counts().values
    fig = px.pie(data_frame=df, values=values, names=labels, title=title,
                 color_discrete_sequence=px.colors.sequential.RdBu_r)
    pie_plot = plot(fig, output_type="div")
    return pie_plot


def data_exploration(request):
    """Wyswietlanie wynikow eksploracji danych"""
    return render(request, 'dataExploration.html')


def getSession(request):
    """Tworzenie klucza sesji"""
    request.session.create()
    sessionKey = request.session.session_key
    return sessionKey


def general(request):
    """Wyswietlanie pytan ogolnych"""
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
    return render(request, 'forms.html', context)


def patient(request):
    """Wyswietlanie pytan dla pacjenta"""
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
    return render(request, 'forms.html', context)


def doctor(request):
    """Wyswietlanie pytan dla lekarza"""
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
    return render(request, 'forms.html', context)


def allGroups(request):
    """Wyswietlanie pytan koncowych"""
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
    return render(request, 'forms.html', context)


def thankYou(request):
    """Wyswietlanie podziekowania za wypelnienie ankiety"""
    return render(request, 'thankYou.html')

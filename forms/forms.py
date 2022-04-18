from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Div
from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from .models import General, Patient, Doctor, AllGroups


class GeneralForm(forms.ModelForm):
    gender = forms.ChoiceField(label='Płeć: ',
                               choices=[('female', 'Kobieta'),
                                        ('male', 'Mężczyzna'),
                                        ('preferNotToSay', 'Wolę nie mówić')],
                               widget=forms.RadioSelect)
    age = forms.ChoiceField(label='Wiek: ',
                            choices=[('18-25', '18-25'),
                                     ('26-35', '26-35'),
                                     ('51-65', '51-65'),
                                     ('>65', '> 65')],
                            widget=forms.RadioSelect)
    residence = forms.ChoiceField(label='Miejsce zamieszkania: ',
                                  choices=[('wieś', 'Wieś'),
                                           ('<10k', 'Miasto do 10 tys. mieszkańców'),
                                           ('<50k', 'Miasto do 50 tys. mieszkańców'),
                                           ('<100k', 'Miasto do 100 tys. mieszkańców'),
                                           ('<500k', 'Miasto do 500 tys. mieszkańców'),
                                           ('>500k.', 'Miasto powyżej 500 tys. mieszkańców')],
                                  widget=forms.RadioSelect)
    whoIsRespondent = forms.ChoiceField(label='Jestem: ',
                                        choices=[('patient', 'Pacjentem'),
                                                 ('doctor', 'Lekarzem')],
                                        widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'gender',
            'age',
            'residence',
            'whoIsRespondent',

            Div(
                FormActions(
                    Button('back', 'Wstecz', css_class='buttonBack ',
                           onClick="javascript:history.go(-1);"),
                    Submit('goNext', 'Dalej', css_class='button')
                ),
                css_class='buttons',
            )
        )

    class Meta:
        model = General
        fields = '__all__'


class PatientForm(forms.ModelForm):
    options = [(True, 'Tak'), (False, 'Nie')]
    usePOZ = forms.ChoiceField(label='Czy korzysta Pan/Pani z Podstawowej Opieki Zdrowotnej? ',
                               choices=options,
                               widget=forms.RadioSelect)
    freqOfVisits = forms.ChoiceField(label='Czy wizyty w POZ są:',
                                     choices=[('Regular', 'Regularne (5-6 razy w roku)'),
                                              ('Occasional', 'Sporadyczne')],
                                     widget=forms.RadioSelect)
    isPunctual = forms.ChoiceField(label='Czy umawiając się na teleporadę pamiętał/a Pan/Pani o punktualności? ',
                                   choices=options,
                                   widget=forms.RadioSelect)
    correctDateOfEConsultation = forms.ChoiceField(label='Czy teleporada odbyła się w terminie zgodnym z wyznaczonym '
                                                         'przy rejestracji terminem? ',
                                                   choices=options,
                                                   widget=forms.RadioSelect)
    isProblemResolved = forms.ChoiceField(label='Czy problem zdrowotny zgłoszony przez Pana/Panią drogą teleporady '
                                                'został rozwiązany? ',
                                          choices=options,
                                          widget=forms.RadioSelect)
    wasVisitProposed = forms.ChoiceField(label='Czy w sytuacji, gdy teleporada nie rozwiązała w pełni Pana/Pani '
                                               'problemu zdrowotnego zaoferowano możliwość wizyty osobistej? ',
                                         choices=options,
                                         widget=forms.RadioSelect)
    wereInstructionsClear = forms.ChoiceField(label='Czy lekarz w sposób jasny i zrozumiały udzielił Panu/Pani '
                                                    'informacji na temat problemu zdrowotnego?',
                                              choices=options,
                                              widget=forms.RadioSelect)
    purposeOfEConsultation = forms.ChoiceField(widget=forms.RadioSelect,
                                               label='W jakim celu najczęściej korzystał/a Pan/Pani z teleporady? ',
                                               choices=[('prescription', 'przedłużenie recepty na leki stałe,'),
                                                        ('consultOfTestResults', 'konsultacja wyników badań,'),
                                                        ('referralToSpecialist',
                                                         'otrzymanie skierowania do lekarza specjalisty,'),
                                                        ('generalConsultation',
                                                         'omówienie aktualnego stanu swojego zdrowia.')])
    useOfETechniques = forms.ChoiceField(widget=forms.RadioSelect,
                                         label='Czy za pomocą teleporady otrzymał/a Pan/Pani e-zwolnienie/e-receptę/'
                                               'e-skierowanie? ',
                                         choices=options)
    isPreparedBeforeEConsultation = forms.ChoiceField(widget=forms.RadioSelect,
                                                      label='Czy przygotował się Pan/Pani do rozmowy z lekarzem? '
                                                            '(np. miał/a Pan/pani przygotowany nr PESEL do '
                                                            'weryfikacji tożsamości, kartkę i długopis, dzienniczek '
                                                            'samokontroli, wyniki badań, listę leków) ',
                                                      choices=options)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'usePOZ',
            'freqOfVisits',
            'isPunctual',
            'correctDateOfEConsultation',
            'isProblemResolved',
            'wasVisitProposed',
            'wereInstructionsClear',
            'purposeOfEConsultation',
            'useOfETechniques',
            'isPreparedBeforeEConsultation',
            Div(
                FormActions(
                    Button('back', 'Wstecz', css_class='buttonBack ',
                           onClick="javascript:history.go(-1);"),
                    Submit('goNext', 'Dalej', css_class='button')
                ),
                css_class='buttons',
            )
        )

    class Meta:
        model = Patient
        fields = '__all__'


class DoctorForm(forms.ModelForm):
    options = [(True, 'Tak'), (False, 'Nie')]
    options1 = [(True, 'Tak'), (False, 'Nie'), ('NoOpinion', 'Nie mam zdania')]
    numberOfEConsults = forms.CharField(widget=forms.TextInput,
                                        label=mark_safe('Przeciętna dzienna liczba: <br/>'
                                                        '&emsp;1. teleporad: '))
    numberOfVisits = forms.CharField(widget=forms.TextInput,
                                     label='&emsp;2. wizyt stacjonarnych: ')
    technicalSkillsRating = forms.ChoiceField(label='Jak Pan/Pani ocenia swoje umiejętności techniczne? ',
                                              choices=[(1, 'bardzo źle'), (2, 'źle'), (3, 'przeciętnie'),
                                                       (4, 'dobrze'), (5, 'bardzo dobrze')],
                                              widget=forms.RadioSelect)
    howManyEConsultsNeedingVisits = forms.CharField(widget=forms.TextInput,
                                                    label='Ile procent teleporad wymaga '
                                                          'umówienia wizyty stacjonarnej? ',
                                                    help_text="Wpisz liczbę całkowitą z zakresu 0-100")

    arePatientsPrepared = forms.ChoiceField(label='Czy pacjenci są przygotowani do rozmowy z lekarzem? ',
                                            choices=options,
                                            widget=forms.RadioSelect)
    howManyPatientsDontAnswer = forms.CharField(widget=forms.TextInput,
                                                label='Jaki procent pacjentów nie odbiera '
                                                      'telefonów? ', help_text="Wpisz liczbę całkowitą z zakresu 0-100",
                                                )

    seriousnessOfPatients = forms.ChoiceField(label='Czy Pani/Pana zdaniem pacjenci traktują teleporady mniej poważnie '
                                                    'niż wizyty stacjonarne? ',
                                              choices=[(True, 'Tak'), (False, 'Nie'),
                                                       ('NoOpinion', 'Nie mam zdania')],
                                              widget=forms.RadioSelect)

    cancellingIfNoContact = forms.ChoiceField(label='Czy brak kontaktu z pacjentem w ustalonym terminie powinien '
                                                    'skutkować anulowaniem wizyty? ',
                                              choices=options,
                                              widget=forms.RadioSelect)
    limitedTrust = forms.ChoiceField(label='Czy lekarz, bazując jedynie na kontakcie werbalnym z pacjentem, '
                                           'powinien stosować zasadę ograniczonego zaufania? ',
                                     choices=options,
                                     widget=forms.RadioSelect)

    eTechniquesAndTimeEfficiency = forms.ChoiceField(
        label=mark_safe('Czy stosowanie e-technik: e-recepty, e-skierowania, '
                        'e-zwolnienia: <br/>&emsp;1. powodują oszczędność czasu?'),
        choices=options,
        widget=forms.RadioSelect)

    eTechniquesAndWorkEase = forms.ChoiceField(label='&emsp;2. ułatwiają pracę?',
                                               choices=options,
                                               widget=forms.RadioSelect)

    fearOfReturning = forms.ChoiceField(label='Czy ma Pan/Pani obawy związane z powrotem do przeprowadzania wizyt w '
                                              'trybie stacjonarnym? ',
                                        choices=options,
                                        widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'numberOfEConsults',
            'numberOfVisits',
            'technicalSkillsRating',
            'howManyEConsultsNeedingVisits',
            'arePatientsPrepared',
            'howManyPatientsDontAnswer',
            'seriousnessOfPatients',
            'cancellingIfNoContact',
            'limitedTrust',
            'eTechniquesAndTimeEfficiency',
            'eTechniquesAndWorkEase',
            'fearOfReturning',
            Div(
                FormActions(
                    Button('back', 'Wstecz', css_class='buttonBack ',
                           onClick="javascript:history.go(-1);"),
                    Submit('goNext', 'Dalej', css_class='button')
                ),
                css_class='buttons',
            )
        )

    def clean_numberOfEConsults(self):
        data = self.cleaned_data['numberOfEConsults']
        if not data.isdecimal():
            raise ValidationError('Wpisana wartość nie jest liczbą naturalną')
        return data

    def clean_numberOfVisits(self):
        data = self.cleaned_data['numberOfVisits']
        if not data.isdecimal():
            raise ValidationError('Wpisana wartość nie jest liczbą naturalną')
        return data

    def clean_howManyEConsultsNeedingVisits(self):
        data = self.cleaned_data['howManyEConsultsNeedingVisits']
        if not data.lstrip("-").isdigit():
            raise ValidationError('Wpisana wartość nie jest liczbą naturalną')
        else:
            if int(data) < 0 or int(data) > 100:
                raise ValidationError('Wpisana wartość jest spoza zakresu 0-100')
        return data

    def clean_howManyPatientsDontAnswer(self):
        data = self.cleaned_data['howManyPatientsDontAnswer']
        if not data.lstrip("-").isdigit():
            raise ValidationError('Wpisana wartość nie jest liczbą naturalną')
        else:
            if int(data) < 0 or int(data) > 100:
                raise ValidationError('Wpisana wartość jest spoza zakresu 0-100')
        return data

    class Meta:
        model = Doctor
        fields = '__all__'


class AllGroupsForm(forms.ModelForm):
    options = [(True, 'Tak'), (False, 'Nie')]
    options1 = [(True, 'Tak'), (False, 'Nie'), ('NoOpinion', 'Nie mam zdania')]
    didTechnicalProblemsOccur = forms.ChoiceField(label='Czy podczas teleporady występowały problemy z połączeniem '
                                                        'telefonicznym? ',
                                                  choices=options,
                                                  widget=forms.RadioSelect)

    eConsultationVsVisit = forms.ChoiceField(label='Co Pan/Pani woli? ',
                                             choices=[('eConsultation', 'teleporada'), ('visit', 'wizyta stacjonarna')],
                                             widget=forms.RadioSelect)

    eConsultationAsStandard = forms.ChoiceField(label='Czy chciałby/chciałaby Pan/Pani, aby teleporada pozostała nadal '
                                                      'standardem? ',
                                                choices=options1,
                                                widget=forms.RadioSelect)

    accessibilityVsLimitingEConsults = forms.ChoiceField(
        label='Czy ograniczenie teleporad spowoduje pogorszenie już i tak trudnego dostępu do lekarzy specjalistów?',
        # todo poprawić
        choices=options1,
        widget=forms.RadioSelect)

    eConsultationVsChildren = forms.ChoiceField(label='Czy nadużywanie teleporad może nieść negatywne konsekwencje dla '
                                                      'osób starszych i dzieci? ',
                                                choices=options1,
                                                widget=forms.RadioSelect)

    queuesAndVisits = forms.ChoiceField(label='Czy obowiązek konsultowania każdego nowego problemu zdrowotnego '
                                              'stacjonarnie oznaczać może powrót kolejek i przepełnionych przychodni? ',
                                        choices=options1,
                                        widget=forms.RadioSelect)

    whoDecidesWhichForm = forms.ChoiceField(label='Kto powinien decydować o formie wizyty? ',
                                            choices=[('patient', 'Pacjent'), ('doctor', 'Lekarz')],
                                            widget=forms.RadioSelect)

    comments = forms.CharField(widget=forms.Textarea,
                               label='Uwagi końcowe - co należałoby poprawić w systemie teleporad? ', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'didTechnicalProblemsOccur',
            'eConsultationVsVisit',
            'eConsultationAsStandard',
            'accessibilityVsLimitingEConsults',
            'eConsultationVsChildren',
            'queuesAndVisits',
            'whoDecidesWhichForm',
            'comments',

            Div(
                FormActions(
                    Button('back', 'Wstecz', css_class='buttonBack ',
                           onClick="javascript:history.go(-1);"),
                    Submit('goNext', 'Dalej', css_class='button')
                ),
                css_class='buttons',
            )
        )

    class Meta:
        model = AllGroups
        fields = '__all__'

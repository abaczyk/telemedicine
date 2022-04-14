from crispy_forms.bootstrap import FormActions
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe


class Main(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Button('goToForm', 'Przejdź do ankiety')
        )


class GeneralForm(forms.Form):
    gender = forms.ChoiceField(label='Płeć',
                               choices=[('kobieta', 'Kobieta'),
                                        ('mężczyzna', 'Mężczyzna'),
                                        ('wolę nie mówić', 'Wolę nie mówić')],
                               widget=forms.RadioSelect)
    age = forms.ChoiceField(label='Wiek',
                            choices=[('18-25', '18-25'),
                                     ('26-35', '26-35'),
                                     ('51-65', '51-65'),
                                     ('>65', '>65')],
                            widget=forms.RadioSelect)
    residence = forms.ChoiceField(label='Miejsce zamieszkania ',
                                  choices=[('wieś', 'Wieś'),
                                           ('<10tys.', 'Miasto do 10 tys. mieszkańców'),
                                           ('<50tys.', 'Miasto do 50 tys. mieszkańców'),
                                           ('<100tys.', 'Miasto do 100 tys. mieszkańców'),
                                           ('<500tys.', 'Miasto do 500 tys. mieszkańców'),
                                           ('>500tys.', 'Miasto powyżej 500 tys. mieszkańców')],
                                  widget=forms.RadioSelect)
    whoIsRespondent = forms.ChoiceField(label='Jestem',
                                        choices=[('Pacjent', 'Pacjentem'),
                                                 ('Lekarz', 'Lekarzem')],
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

            FormActions(
                Submit('goNext', 'Przejdź dalej', css_class='btn-default'),
                # TODO opracować przechodzenie do innych stron
            )
        )


class PatientForm(forms.Form):
    options = [(True, 'Tak'), (False, 'Nie')]
    usePOZ = forms.ChoiceField(label='Czy korzysta Pan/Pani z Podstawowej Opieki Zdrowotnej?',
                               choices=options,
                               widget=forms.RadioSelect)
    freqOfVisits = forms.ChoiceField(label='Czy wizyty w POZ są:',
                                     choices=[('Regular', 'Regularne (5-6 razy w roku)'), ('Occasional','Sporadyczne')],
                                     widget=forms.RadioSelect)
    isPunctual = forms.ChoiceField(label='Czy umawiając się na teleporadę pamiętał/a Pan/Pani o punktualności?',
                                   choices=options,
                                   widget=forms.RadioSelect)
    correctDateOfEConsultation = forms.ChoiceField(label='Czy teleporada odbyła się w terminie zgodnym z wyznaczonym '
                                                         'przy rejestracji terminem?',
                                                   choices=options,
                                                   widget=forms.RadioSelect)
    isProblemResolved = forms.ChoiceField(label='Czy problem zdrowotny zgłoszony przez Pana/Panią drogą teleporady '
                                                'został rozwiązany?',
                                          choices=options,
                                          widget=forms.RadioSelect)
    wasVisitProposed = forms.ChoiceField(label='Czy w sytuacji, gdy teleporada nie rozwiązała w pełni Pana/Pani '
                                               'problemu zdrowotnego zaoferowano możliwość wizyty osobistej?',
                                         choices=options,
                                         widget=forms.RadioSelect)
    wereInstructionsClear = forms.ChoiceField(label='Czy lekarz w sposób jasny i zrozumiały udzielił Panu/Pani '
                                                   'informacji na temat problemu zdrowotnego?',
                                             choices=options,
                                             widget=forms.RadioSelect)
    purposeOfEConsultation = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                       label='W jakim celu zazwyczaj korzystał/a Pan/Pani z teleporady?',
                                                       choices=[('prescription', 'przedłużenie recepty na leki stałe,'),
                                                                ('consultOfTestResults', 'konsultacja wyników badań,'),
                                                                ('referralToSpecialist',
                                                                 'otrzymanie skierowania do lekarza specjalisty,'),
                                                                ('generalConsultation',
                                                                 'omówienie aktualnego stanu swojego zdrowia.')])
    useOfETechniques = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                 label='Czy za pomocą teleporady otrzymał/a Pan/Pani:',
                                                 choices=[('e-sickLeave', 'e-zwolnienie,'),
                                                          ('e-presctiption', 'e-receptę,'),
                                                          ('e-referral', 'e-skierowanie?')])
    preparationBeforeConsultation = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                              label='Czy przygotował Pan/Pani do rozmowy z lekarzem: ',
                                                              choices=[('PESEL', 'PESEL do identyfikacji tożsamości,'),
                                                                       ('penAndPaper', 'kartkę i długopis,'),
                                                                       ('self-controlJournal',
                                                                        'dzienniczek samokontroli,'),
                                                                       ('testResults', 'wyniki badań,'),
                                                                       ('listOfMedicine', 'listę leków,'),
                                                                       ('listOfQuestions',
                                                                        'spis pytań do lekarza.')])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'usePOZ',
            'freqOfVisits',
            'correctDateOfEConsultation',
            'isProblemResolved',
            'wasVisitProposed',
            'wereInstructionsClear',
            'purposeOfEConsultation',
            'useOfETechniques',
            'preparationBeforeConsultation',

            FormActions(
                Submit('goNext', 'Przejdź dalej', css_class='btn-default'),
            )
        )


class DoctorForm(forms.Form):
    options = [(True, 'Tak'), (False, 'Nie')]
    numberOfEConsults = forms.CharField(widget=forms.TextInput, label=mark_safe('Przeciętna dzienna liczba: <br/>'
                                                                                'teleporad: '))
    numberOfVisits = forms.CharField(widget=forms.TextInput, label='wizyt stacjonarnych: ') #TODO dać wcięcie
    technicalSkillsRating = forms.ChoiceField(label='Jak Pan/Pani ocenia swoje umiejętności techniczne?',
                                              choices=[(1, 'bardzo źle'), (2, 'źle'), (3, 'przeciętnie'),
                                                       (4, 'dobrze'), (5, 'bardzo dobrze')],
                                              # TODO ustawić jedno obok drugiego
                                              widget=forms.RadioSelect)
    howManyEConsultsNeedingVisits = forms.CharField(widget=forms.TextInput, label='Ile procent teleporad wymaga '
                                                                                  'umówienia wizyty stacjonarnej?')

    arePatientsPrepared = forms.ChoiceField(label='Czy pacjenci są przygotowani do rozmowy z lekarzem?',
                                            choices=options,
                                            widget=forms.RadioSelect)
    howManyPatientsDontAnswer = forms.CharField(widget=forms.TextInput, label='Jaki procent pacjentów nie odbiera '
                                                                              'telefonów?')

    seriousnessOfPatients = forms.ChoiceField(label='Czy Pani/Pana zdaniem pacjenci traktują teleporady mniej poważnie '
                                                    'niż wizyty stacjonarne?',
                                              choices=[(True, 'Tak'), (False, 'Nie'),
                                                       ('NoOpinion', 'Nie mam zdania')],
                                              widget=forms.RadioSelect)

    cancellingIfNoContact = forms.ChoiceField(label='Czy brak kontaktu z pacjentem w ustalonym terminie powinien '
                                                    'skutkować anulowaniem wizyty?',
                                              choices=options,
                                              widget=forms.RadioSelect)
    limitedTrust = forms.ChoiceField(label='Czy lekarz, bazując jedynie na kontakcie werbalnym z pacjentem, '
                                           'powinien stosować zasadę ograniczonego zaufania?',
                                     choices=options,
                                     widget=forms.RadioSelect)

    eTechniquesAndTimeEfficiency = forms.ChoiceField(label=mark_safe('Czy stosowanie e-technik: e-recepty, e-skierowania, '
                                                           'e-zwolnienia: <br/>powodują oszczędność czasu?'), #TODO dać wcięcie
                                                     choices=options,
                                                     widget=forms.RadioSelect)

    eTechniquesAndWorkEase = forms.ChoiceField(label='ułatwiają pracę?',
                                               choices=options,
                                               widget=forms.RadioSelect)

    fearOfReturning = forms.ChoiceField(label='Czy ma Pan/Pani obawy związane z powrotem do przeprowadzania wizyt w '
                                              'trybie stacjonarnym?',
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
            'percentOfEConsultsNeedingVisits',
            'arePatientsPrepared',
            'howManyPatientsDontAnswer',
            'seriousnessOfPatients',
            'cancellingIfNoContact',
            'limitedTrust',
            'eTechniquesAndTimeEfficiency',
            'eTechniquesAndWorkEase',
            'fearOfReturning',

            FormActions(
                Submit('goNext', 'Przejdź dalej', css_class='btn-default'),
            )
        )


class AllGroupsForm(forms.Form):
    options = [(True, 'Tak'), (False, 'Nie')]
    options1 = [('True', 'Tak'), ('False', 'Nie'), ('NoOpinion', 'Nie mam zdania')]
    didTechnicalProblemsOccur = forms.ChoiceField(label='Czy podczas teleporady występowały problemy z połączeniem '
                                                        'telefonicznym?',
                                                  choices=options,
                                                  widget=forms.RadioSelect)

    eConsultationVsVisit = forms.ChoiceField(label='Co Pan/Pani woli?',
                                             choices=[('eConsultation', 'teleporada'), ('visit', 'wizyta stacjonarna')],
                                             widget=forms.RadioSelect)

    eConsultationAsStandard = forms.ChoiceField(label='Czy chciałby/chciałaby Pan/Pani, aby teleporada pozostała nadal '
                                                      'standardem?',
                                                choices=options1,
                                                widget=forms.RadioSelect)

    accessibilityVsLimitingEConsults = forms.ChoiceField(
        label='Czy ograniczenie teleporad spowoduje pogorszenie już i tak trudnego dostępu do lekarzy specjalistów?',
        choices=options1,
        widget=forms.RadioSelect)

    eConsultationVsChildren = forms.ChoiceField(label='Czy nadużywanie teleporad może nieść negatywne konsekwencje dla '
                                                      'osób starszych i dzieci? ',
                                                choices=options1,
                                                widget=forms.RadioSelect)

    queuesAndVisits = forms.ChoiceField(label='Czy obowiązek konsultowania każdego nowego problemu zdrowotnego '
                                              'stacjonarnie oznaczać może powrót kolejek i przepełnionych przychodni?',
                                        choices=options1,
                                        widget=forms.RadioSelect)

    whoDecidesWhichForm = forms.ChoiceField(label='Kto powinien decydować o formie wizyty?',
                                            choices=[('patient', 'Pacjent'), ('doctor', 'Lekarz')],
                                            widget=forms.RadioSelect)

    comments = forms.CharField(widget=forms.Textarea,
                               label='Uwagi końcowe - co należałoby poprawić w systemie teleporad?')

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

            FormActions(
                Submit('submit', 'Wyślij', css_class='btn-default'),
            )
        )

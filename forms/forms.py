from crispy_forms.bootstrap import FormActions
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from django.http import HttpResponseRedirect


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
    options = [('yes', 'Tak'), ('no', 'Nie')]
    usePOZ = forms.ChoiceField(label='Czy korzysta Pan/Pani z Podstawowej Opieki Zdrowotnej?',
                               choices=options,
                               widget=forms.RadioSelect)

    freqOfVisits = forms.ChoiceField(label='Czy wizyty w POZ są:',
                                     choices=[('regularne', 'Regularne (5-6 razy w roku)')],
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

    areInstructionsClear = forms.ChoiceField(label='Czy lekarz w sposób jasny i zrozumiały udzielił Panu/Pani '
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

    useOfETools = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
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
                                                                       ('listOfQuestionsToDoctor',
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
            'areInstructionsClear',
            'purposeOfEConsultation',
            'useOfETools',
            'preparationBeforeConsultation',

            FormActions(
                Button('goNext', 'Przejdź dalej', css_class='btn-default'),

            )
        )


class DoctorForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(

            FormActions(
                Submit('goNext', 'Przejdź dalej', css_class='btn-default'),
            )
        )


class AllGroupsForm(forms.Form):
    options = [('yes', 'Tak'), ('no', 'Nie')]

    didTechnicalProblemsOccur = forms.ChoiceField(label='Czy podczas teleporady występowały problemy z połączeniem '
                                                        'telefonicznym?',
                                                  choices=options,
                                                  widget=forms.RadioSelect)

    eConsultationVsVisit = forms.ChoiceField(label='Co Pan/Pani woli?',
                                             choices=[('eConsultation', 'teleporada'), ('visit', 'wizyta stacjonarna')],
                                             widget=forms.RadioSelect)

    eConsultationAsStandard = forms.ChoiceField(label='Czy chciałby/chciałaby Pan/Pani, aby teleporada pozostała nadal '
                                                      'standardem?',
                                                choices=[('yes', 'Tak'), ('no', 'Nie'),
                                                         ('noOpinion', 'Nie mam zdania')],
                                                widget=forms.RadioSelect)

    accessibilityVsLimitingEConsults = forms.ChoiceField(
        label='Czy ograniczenie teleporad spowoduje pogorszenie już i tak trudnego dostępu do lekarzy specjalistów?',
        choices=[('yes', 'Tak'), ('no', 'Nie'), ('noOpinion', 'Nie mam zdania')],
        widget=forms.RadioSelect)

    eConsultationVsChildren = forms.ChoiceField(label='Czy nadużywanie teleporad może nieść negatywne konsekwencje dla '
                                                      'osób starszych i dzieci? ',
                                                choices=options,
                                                widget=forms.RadioSelect)

    queuesAndVisits = forms.ChoiceField(label='Czy obowiązek konsultowania każdego nowego problemu zdrowotnego '
                                              'stacjonarnie oznaczać może powrót kolejek i przepełnionych przychodni?',
                                        choices=[('yes', 'Tak'), ('no', 'Nie'), ('noOpinion', 'Nie mam zdania')],
                                        widget=forms.RadioSelect)

    whoDecidesWhichForm = forms.ChoiceField(label='Kto powinien decydować o formie wizyty?',
                                        choices=[('patient', 'Pacjent'), ('doctor', 'Lekarz')],
                                        widget=forms.RadioSelect)

    comments = forms.CharField(widget=forms.Textarea, label='Uwagi końcowe - co należałoby poprawić w systemie teleporad?')

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

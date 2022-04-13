from crispy_forms.bootstrap import FormActions
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class Main(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Submit('goToForm', 'Przejdź do ankiety')
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
    options = [('tak', 'Tak'), ('nie', 'Nie')]
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
                Submit('goNext', 'Przejdź dalej', css_class='btn-default'),
            )
        )


class DoctorForm(forms.Form):
    name = forms.CharField()


class AllGroupsForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            FormActions(
                Submit('submit', 'Wyślij', css_class='btn-default'),
            )
        )

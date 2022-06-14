""" Anna Baczyk 180849
Plik umozliwiajacy tworzenie pol w poszczegolnych ankietach"""

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from .models import General, Patient, Doctor, AllGroups


class GeneralForm(forms.ModelForm):
    """Tworzenie poszczegolnych pol w pytaniach ogolnych"""
    gender = forms.ChoiceField(label='Płeć:',
                               choices=[('Female', 'Kobieta'),
                                        ('Male', 'Mężczyzna'),
                                        ('PreferNotToSay', 'Wolę nie mówić')],
                               widget=forms.RadioSelect)
    age = forms.ChoiceField(label='Wiek:',
                            choices=[('18-25', '18-25'),
                                     ('26-35', '26-35'),
                                     ('36-45', '36-45'),
                                     ('46-55', '46-55'),
                                     ('56-65', '56-65'),
                                     ('>65', '> 65')],
                            widget=forms.RadioSelect)
    residence = forms.ChoiceField(label='Miejsce zamieszkania:',
                                  choices=[('Village', 'Wieś'),
                                           ('<10k', 'Miasto do 10 tys. mieszkańców'),
                                           ('<50k', 'Miasto do 50 tys. mieszkańców'),
                                           ('<100k', 'Miasto do 100 tys. mieszkańców'),
                                           ('<500k', 'Miasto do 500 tys. mieszkańców'),
                                           ('>500k', 'Miasto powyżej 500 tys. mieszkańców')],
                                  widget=forms.RadioSelect)
    employment = forms.ChoiceField(widget=forms.RadioSelect,
                                   label='Status zatrudnienia: ',
                                   choices=[('Employed', 'Pracujący'),
                                            ('Unemployed', 'Bezrobotny'),
                                            ('Student', 'Uczeń/student')])
    education = forms.ChoiceField(widget=forms.RadioSelect,
                                  label='Wykształcenie: ',
                                  choices=[('Primary', 'Podstawowe'),
                                           ('Vocational', 'Zasadnicze zawodowe'),
                                           ('Secondary', 'Średnie'),
                                           ('University', 'Wyższe')])
    whoIsRespondent = forms.ChoiceField(label='Jestem:',
                                        choices=[('Patient', 'Pacjentem'),
                                                 ('Doctor', 'Lekarzem')],
                                        widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        # wykorzystanie Crispy Forms do ulatwienia rozmieszczenia poszczegolnych pol
        self.helper.layout = Layout(
            'gender',
            'age',
            'residence',
            'employment',
            'education',
            'whoIsRespondent',

            # utworzenie przyciskow cofania i przejscia dalej
            FormActions(
                Button('back', 'Wstecz', css_class='buttonBack ',
                       onClick="javascript:history.go(-1);"),
                Submit('goNext', 'Dalej', css_class='button'),
                css_class='buttons',
            )
        )

    class Meta:
        """Powiazanie bazy danych z pytaniami"""
        model = General
        fields = '__all__'


class PatientForm(forms.ModelForm):
    """Tworzenie poszczegolnych pol w pytaniach dla pacjenta"""
    options = [(True, 'Tak'), (False, 'Nie')]
    options1 = [(True, 'Tak'), (False, 'Nie'), ('NoOpinion', 'Nie mam zdania')]
    usePOZ = forms.ChoiceField(label='Czy korzysta Pan/Pani z Podstawowej Opieki Zdrowotnej?',
                               choices=options,
                               widget=forms.RadioSelect)
    freqOfVisits = forms.ChoiceField(label='Czy wizyty w POZ są:',
                                     choices=[('Regular', 'Regularne (5-6 razy w roku)'),
                                              ('Occasional', 'Sporadyczne')],
                                     widget=forms.RadioSelect)
    isPunctual = forms.ChoiceField(label='Czy umawiając się na teleporadę pamiętał/a Pan/Pani o punktualności?',
                                   choices=options,
                                   widget=forms.RadioSelect)
    whenWasEConsultation = forms.ChoiceField(widget=forms.RadioSelect, label='Kiedy przeważnie odbywała się teleporada '
                                                                             'w odniesieniu do terminu rejestracji?',
                                             choices=[('SameDay', 'Tego samego dnia'),
                                                      ('NextDay', 'Następnego dnia'),
                                                      ('Within3Days', 'W ciągu 3 kolejnych dni'),
                                                      ('WithinWeek', 'W ciągu tygodnia'),
                                                      ('Later', 'Później')])
    correctDateOfEConsultation = forms.ChoiceField(label='Czy teleporada na ogół odbywała się w terminie zgodnym '
                                                         'z wyznaczonym przy rejestracji?',
                                                   choices=options,
                                                   widget=forms.RadioSelect)
    isProblemResolved = forms.ChoiceField(label='Czy problem zdrowotny zgłoszony przez Pana/Panią drogą teleporady '
                                                'był w większości przypadków rozwiązany?',
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
    wasDoctorEngaged = forms.ChoiceField(widget=forms.RadioSelect,
                                         label='Czy odczuł/a Pan/Pani, że zaangażowanie lekarza jest mniejsze przy '
                                               'przeprowadzeniu teleporady niż w przypadku wizyty stacjonarnej?',
                                         choices=options1)
    purposeOfEConsultation = forms.ChoiceField(widget=forms.RadioSelect,
                                               label='W jakim celu najczęściej korzystał/a Pan/Pani z teleporady?',
                                               choices=[('Prescription', 'Przedłużenie recepty na leki stałe,'),
                                                        ('ConsultOfTestResults', 'Konsultacja wyników badań,'),
                                                        ('ReferralToSpecialist',
                                                         'Otrzymanie skierowania do lekarza specjalisty,'),
                                                        ('GeneralConsultation',
                                                         'Omówienie aktualnego stanu swojego zdrowia.')])
    useOfETechniques = forms.ChoiceField(widget=forms.RadioSelect,
                                         label='Czy za pomocą teleporady otrzymał/a Pan/Pani e-zwolnienie/e-receptę/'
                                               'e-skierowanie?',
                                         choices=options)
    isPreparedBeforeEConsultation = forms.ChoiceField(widget=forms.RadioSelect,
                                                      label='Czy przygotował się Pan/Pani do rozmowy z lekarzem? '
                                                            '(np. miał/a Pan/pani przygotowany nr PESEL do '
                                                            'weryfikacji tożsamości, kartkę i długopis, dzienniczek '
                                                            'samokontroli, wyniki badań, listę leków)',
                                                      choices=options)
    fearOfViolatingConfidentiality = forms.ChoiceField(widget=forms.RadioSelect,
                                                       label='Czy obawia się Pan/Pani problemów dotyczących utrzymania '
                                                             'poufności informacji przekazanych podczas teleporady?',
                                                       choices=options1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        # wykorzystanie Crispy Forms do ulatwienia rozmieszczenia poszczegolnych pol
        self.helper.layout = Layout(
            'usePOZ',
            'freqOfVisits',
            'isPunctual',
            'whenWasEConsultation',
            'correctDateOfEConsultation',
            'isProblemResolved',
            'wasVisitProposed',
            'wereInstructionsClear',
            'wasDoctorEngaged',
            'purposeOfEConsultation',
            'useOfETechniques',
            'isPreparedBeforeEConsultation',
            'fearOfViolatingConfidentiality',

            # utworzenie przyciskow cofania i przejscia dalej
            FormActions(
                Button('back', 'Wstecz', css_class='buttonBack ',
                       onClick="javascript:history.go(-1);"),
                Submit('goNext', 'Dalej', css_class='button'),
                css_class='buttons',
            )
        )

    class Meta:
        """Powiazanie bazy danych z pytaniami"""
        model = Patient
        fields = '__all__'


class DoctorForm(forms.ModelForm):
    """Tworzenie poszczegolnych pol w pytaniach dla lekarza"""
    options = [(True, 'Tak'), (False, 'Nie')]
    options1 = [(True, 'Tak'), (False, 'Nie'), ('NoOpinion', 'Nie mam zdania')]
    specializationOptions = [('None', 'Brak'),
                             ('Allergology', 'Alergologia'),
                             ('Anesthesiology and intensive care', 'Anestezjologia i intensywna terapia'),
                             ('Angiology', 'Angiologia'),
                             ('Audiology and phoniatrics', 'Audiologia i foniatria'),
                             ('Balneology and physical medicine', 'Balneologia i medycyna fizykalna'),
                             ('Paediatric surgery', 'Chirurgia dziecięca'),
                             ('Thoracic surgery', 'Chirurgia klatki piersiowej'),
                             ('Vascular Surgery', 'Chirurgia naczyniowa'),
                             ('General Surgery', 'Chirurgia ogólna'),
                             ('Oncology Surgery', 'Chirurgia onkologiczna'),
                             ('Plastic Surgery', 'Chirurgia plastyczna'),
                             ('Maxillofacial Surgery', 'Chirurgia szczękowo-twarzowa'),
                             ('Lung diseases', 'Choroby płuc'),
                             ('Lung diseases of children', 'Choroby płuc dzieci'),
                             ('Internal diseases', 'Choroby wewnętrzne'),
                             ('Infectious diseases', 'Choroby zakaźne'),
                             ('Dermatology and venereology', 'Dermatologia i wenerologia'),
                             ('Diabetology', 'Diabetologia'),
                             ('Laboratory diagnostics', 'Diagnostyka laboratoryjna'),
                             ('Endocrinology', 'Endokrynologia'),
                             ('Gynecologic and reproductive endocrinology',
                              'Endokrynologia ginekologiczna i rozrodczość'),
                             ('Pediatric endocrinology and diabetology', 'Endokrynologia i diabetologia dziecięca'),
                             ('Epidemiology', 'Epidemiologia'),
                             ('Clinical pharmacology', 'Farmakologia kliniczna'),
                             ('Gastroenterology', 'Gastroenterologia'),
                             ('Paediatric gastroenterology', 'Gastroenterologia dziecięca'),
                             ('Clinical genetics', 'Genetyka kliniczna'),
                             ('Geriatrics', 'Geriatria'),
                             ('Gynecology Oncology', 'Ginekologia onkologiczna'),
                             ('Hematology', 'Hematologia'),
                             ('Hypertensiology', 'Hipertensjologia'),
                             ('Clinical immunology', 'Immunologia kliniczna'),
                             ('Intensive care', 'Intensywna terapia'),
                             ('Cardiac surgery', 'Kardiochirurgia'),
                             ('Cardiology', 'Kardiologia'),
                             ('Pediatric cardiology', 'Kardiologia dziecięca'),
                             ('Aviation medicine', 'Medycyna lotnicza'),
                             ('Maritime and tropical medicine', 'Medycyna morska i tropikalna'),
                             ('Nuclear medicine', 'Medycyna nuklearna'),
                             ('Palliative medicine', 'Medycyna paliatywna'),
                             ('Occupational medicine', 'Medycyna pracy'),
                             ('Emergency medicine', 'Medycyna ratunkowa'),
                             ('Family medicine', 'Medycyna rodzinna'),
                             ('Forensic medicine', 'Medycyna sądowa'),
                             ('Sports medicine', 'Medycyna sportowa'),
                             ('Medical microbiology', 'Mikrobiologia lekarska'),
                             ('Nephrology', 'Nefrologia'),
                             ('Paediatric nephrology', 'Nefrologia dziecięca'),
                             ('Neonatology', 'Neonatologia'),
                             ('Neurosurgery', 'Neurochirurgia'),
                             ('Neurology', 'Neurologia'),
                             ('Paediatric neurology', 'Neurologia dziecięca'),
                             ('Neuropathology', 'Neuropatologia'),
                             ('Ophthalmology', 'Okulistyka'),
                             ('Paediatric oncology and haematology', 'Onkologia i hematologia dziecięca'),
                             ('Clinical oncology', 'Onkologia kliniczna'),
                             ('Orthopaedics and traumatology', 'Ortopedia i traumatologia narządu ruchu'),
                             ('Otorhinolaryngology', 'Otorynolaryngologia'),
                             ('Paediatric otorhinolaryngology', 'Otorynolaryngologia dziecięca'),
                             ('Pathomorphology', 'Patomorfologia'),
                             ('Pediatrics', 'Pediatria'),
                             ('Metabolic pediatrics', 'Pediatria metaboliczna'),
                             ('Perinatology', 'Perinatologia'),
                             ('Obstetrics and Gynecology', 'Położnictwo i ginekologia'),
                             ('Psychiatry', 'Psychiatria'),
                             ('Child and adolescent psychiatry', 'Psychiatria dzieci i młodzieży'),
                             ('Radiology and image diagnostics', 'Radiologia i diagnostyka obrazowa'),
                             ('Radiation therapy', 'Radioterapia onkologiczna'),
                             ('Medical rehabilitation', 'Rehabilitacja medyczna'),
                             ('Rheumatology', 'Reumatologia'),
                             ('Sexology', 'Seksuologia'),
                             ('Clinical toxicology', 'Toksykologia kliniczna'),
                             ('Clinical transfusionology', 'Transfuzjologia kliniczna'),
                             ('Clinical transplantology', 'Transplantologia kliniczna'),
                             ('Urology', 'Urologia'),
                             ('Paediatric urology', 'Urologia dziecięca'),
                             ('Public health', 'Zdrowie publiczne')]
    yearsOfExperience = forms.CharField(widget=forms.TextInput,
                                        label='Ile ma Pan/Pani lat doświadczenia?')
    specialization = forms.ChoiceField(label='Wybierz specjalizację', widget=forms.Select,
                                       choices=specializationOptions)
    numberOfEConsults = forms.CharField(widget=forms.TextInput,
                                        label=mark_safe('Przeciętna dzienna liczba: <br/>'
                                                        '&emsp;1. teleporad:'))
    numberOfVisits = forms.CharField(widget=forms.TextInput,
                                     label='&emsp;2. wizyt stacjonarnych:')

    lengthOfEConsults = forms.CharField(widget=forms.TextInput,
                                        label=mark_safe('Przeciętna długość w minutach: <br/>'
                                                        '&emsp;1. teleporady:'))
    lengthOfVisits = forms.CharField(widget=forms.TextInput,
                                     label='&emsp;2. wizyty stacjonarnej:')
    howManyEConsultsNeedingVisits = forms.CharField(widget=forms.TextInput,
                                                    label='Ile procent teleporad miesięcznie wymaga '
                                                          'umówienia wizyty stacjonarnej?',
                                                    help_text="Wpisz liczbę całkowitą z zakresu 0-100")
    technicalSkillsRating = forms.ChoiceField(label='Jak Pan/Pani ocenia swoje umiejętności obsługi komputera?',
                                              choices=[(1, 'Bardzo źle'), (2, 'źle'), (3, 'Przeciętnie'),
                                                       (4, 'Dobrze'), (5, 'Bardzo dobrze')],
                                              widget=forms.RadioSelect)
    arePatientsPrepared = forms.ChoiceField(label='Czy pacjenci są przygotowani do rozmowy z lekarzem?',
                                            choices=options,
                                            widget=forms.RadioSelect)
    howManyPatientsDontAnswer = forms.CharField(widget=forms.TextInput,
                                                label='Jaki procent pacjentów nie odbiera '
                                                      'telefonów?', help_text="Wpisz liczbę całkowitą z zakresu 0-100",
                                                )

    seriousnessOfPatients = forms.ChoiceField(label='Czy Pani/Pana zdaniem pacjenci traktują teleporady mniej poważnie '
                                                    'niż wizyty stacjonarne?',
                                              choices=[(True, 'Tak'), (False, 'Nie'),
                                                       ('NoOpinion', 'Nie mam zdania')],
                                              widget=forms.RadioSelect)

    cancellingIfNoContact = forms.ChoiceField(label='Czy brak kontaktu z pacjentem w ustalonym terminie powinien '
                                                    'skutkować anulowaniem teleporady?',
                                              choices=options,
                                              widget=forms.RadioSelect)
    limitedTrust = forms.ChoiceField(label='Czy lekarz, bazując jedynie na kontakcie werbalnym z pacjentem, '
                                           'powinien stosować zasadę ograniczonego zaufania?',
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

    fearOfReturning = forms.ChoiceField(
        label='Czy ma Pan/Pani obawy związane z powrotem do przeprowadzania wizyt TYLKO w '
              'trybie stacjonarnym?',
        choices=options,
        widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        # wykorzystanie Crispy Forms do ulatwienia rozmieszczenia poszczegolnych pol
        self.helper.layout = Layout(
            'yearsOfExperience',
            'specialization',
            'numberOfEConsults',
            'numberOfVisits',
            'lengthOfEConsults',
            'lengthOfVisits',
            'howManyEConsultsNeedingVisits',
            'technicalSkillsRating',
            'arePatientsPrepared',
            'howManyPatientsDontAnswer',
            'seriousnessOfPatients',
            'cancellingIfNoContact',
            'limitedTrust',
            'eTechniquesAndTimeEfficiency',
            'eTechniquesAndWorkEase',
            'fearOfReturning',

            # utworzenie przyciskow cofania i przejscia dalej
            FormActions(
                Button('back', 'Wstecz', css_class='buttonBack ',
                       onClick="javascript:history.go(-1);"),
                Submit('goNext', 'Dalej', css_class='button'),
                css_class='buttons',
            )
        )

    # funkcje walidujace poprawnosc wprowadzonych danych
    def clean_yearsOfExperience(self):
        """Sprawdzanie. czy zostala podana poprawna wartosc (liczby naturalne)"""
        data = self.cleaned_data['yearsOfExperience']
        if not data.isdecimal():
            raise ValidationError('Wpisana wartość nie jest liczbą naturalną')
        return data

    def clean_numberOfEConsults(self):
        """Sprawdzanie, czy zostala podana poprawna wartosc (liczby naturalne)"""
        data = self.cleaned_data['numberOfEConsults']
        if not data.isdecimal():
            raise ValidationError('Wpisana wartość nie jest liczbą naturalną')
        return data

    def clean_numberOfVisits(self):
        """Sprawdzanie, czy zostala podana poprawna wartosc (liczby naturalne)"""
        data = self.cleaned_data['numberOfVisits']
        if not data.isdecimal():
            raise ValidationError('Wpisana wartość nie jest liczbą naturalną')
        return data

    def clean_lengthOfEConsults(self):
        """Sprawdzanie, czy zostala podana poprawna wartosc (liczby naturalne)"""
        data = self.cleaned_data['lengthOfEConsults']
        if not data.isdecimal():
            raise ValidationError('Wpisana wartość nie jest liczbą naturalną')
        return data

    def clean_lengthOfVisits(self):
        """Sprawdzanie, czy zostala podana poprawna wartosc (liczby naturalne)"""
        data = self.cleaned_data['lengthOfVisits']
        if not data.isdecimal():
            raise ValidationError('Wpisana wartość nie jest liczbą naturalną')
        return data

    def clean_howManyEConsultsNeedingVisits(self):
        """Sprawdzanie, czy zostala podana poprawna wartosc (liczby naturalne mniejsze od 100)"""
        data = self.cleaned_data['howManyEConsultsNeedingVisits']
        data = data.lstrip("%")
        if not data.isdigit():
            raise ValidationError('Wpisana wartość nie jest liczbą naturalną')
        else:
            if int(data) < 0 or int(data) > 100:  # sprawdzenie, czy liczba miesci sie w zakresie 0 - 100
                raise ValidationError('Wpisana wartość jest spoza zakresu 0-100')
        return data

    def clean_howManyPatientsDontAnswer(self):
        """Sprawdzanie, czy zostala podana poprawna wartosc (liczby naturalne mniejsze od 100)"""
        data = self.cleaned_data['howManyPatientsDontAnswer']
        data = data.lstrip("%")
        if not data.isdigit():
            raise ValidationError('Wpisana wartość nie jest liczbą naturalną')
        else:
            if int(data) < 0 or int(data) > 100:
                raise ValidationError('Wpisana wartość jest spoza zakresu 0-100')
        return data

    class Meta:
        """Powiazanie bazy danych z pytaniami"""
        model = Doctor
        fields = '__all__'


class AllGroupsForm(forms.ModelForm):
    """Tworzenie poszczegolnych pol w pytaniach koncowych"""
    options = [(True, 'Tak'), (False, 'Nie')]
    options1 = [(True, 'Tak'), (False, 'Nie'), ('NoOpinion', 'Nie mam zdania')]
    didTechnicalProblemsOccur = forms.ChoiceField(label='Czy podczas teleporady występowały problemy z połączeniem '
                                                        'telefonicznym?',
                                                  choices=options,
                                                  widget=forms.RadioSelect)

    eConsultationVsVisit = forms.ChoiceField(label='Co Pan/Pani woli?',
                                             choices=[('eConsultation', 'Teleporadę'), ('visit', 'Wizytę stacjonarną')],
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
                                                      'osób starszych i dzieci?',
                                                choices=options1,
                                                widget=forms.RadioSelect)

    queuesAndVisits = forms.ChoiceField(label='Czy obowiązek konsultowania każdego nowego problemu zdrowotnego '
                                              'stacjonarnie oznaczać może powrót kolejek i przepełnionych przychodni?',
                                        choices=options1,
                                        widget=forms.RadioSelect)

    whoDecidesWhichForm = forms.ChoiceField(label='Kto powinien decydować o formie wizyty?',
                                            choices=[('patient', 'Pacjent'), ('doctor', 'Lekarz'),
                                                     ('noOpinion', 'Nie mam zdania')],
                                            widget=forms.RadioSelect)

    comments = forms.CharField(widget=forms.Textarea,
                               label='Uwagi końcowe - co należałoby poprawić w systemie teleporad?', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        # wykorzystanie Crispy Forms do ulatwienia rozmieszczenia poszczegolnych pol
        self.helper.layout = Layout(
            'didTechnicalProblemsOccur',
            'eConsultationVsVisit',
            'eConsultationAsStandard',
            'accessibilityVsLimitingEConsults',
            'eConsultationVsChildren',
            'queuesAndVisits',
            'whoDecidesWhichForm',
            'comments',

            # utworzenie przyciskow cofania i przejscia dalej
            FormActions(
                Button('back', 'Wstecz', css_class='buttonBack ',
                       onClick="javascript:history.go(-1);"),
                Submit('goNext', 'Wyślij', css_class='button'),
                css_class='buttons',
            )
        )

    class Meta:
        """Powiazanie bazy danych z pytaniami"""
        model = AllGroups
        fields = '__all__'

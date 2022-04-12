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
                Submit('goNext', 'Przejdź dalej', css_class='btn-default'), #TODO opracować przechodzenie do innych stron
            )
        )

class PatientForm(forms.Form):
    name = forms.CharField()


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

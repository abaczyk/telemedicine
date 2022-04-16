from django.core.exceptions import ValidationError

def validateIfInteger(value):

    if type(value) != int:
        raise ValidationError(f"{value} nie jest liczbą całkowitą")
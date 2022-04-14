from django.db import models

class General(models.Model):
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    residence = models.CharField(max_length=100)
    whoIsRespondent = models.CharField(max_length=100)

class Patient(models.Model):
    respondentId = models.ForeignKey(General, on_delete=models.CASCADE)
    usePOZ = models.BooleanField()
    freqOfVisits = models.CharField(max_length=100)
    isPunctual = models.BooleanField()
    correctDateOfEConsultation = models.BooleanField()



# class Doctor(models.Model):
#
# class AllGroups(models.Model):
#
#
# class PatientForm(forms.ModelForm):
#
#
# def generalQuestions(request):
#
# def patientQuestions(request):
#
# def doctorQuestions(request):
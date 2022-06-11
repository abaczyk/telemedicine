"""Anna Baczyk 180849
Plik zawierajacy informacje o polach w bazie danych"""

from django.db import models


class General(models.Model):
    id = models.AutoField(primary_key=True)
    sessionKey = models.CharField(max_length=100, editable=False)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    residence = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    employment = models.CharField(max_length=100)
    whoIsRespondent = models.CharField(max_length=100)


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    sessionKey = models.CharField(max_length=100, editable=False)
    respondentID = models.OneToOneField(General, on_delete=models.CASCADE,
                                        editable=False)  # powiazanie z tabela general za pomoca respondentID
    usePOZ = models.BooleanField()
    freqOfVisits = models.CharField(max_length=100)
    isPunctual = models.BooleanField()
    whenWasEConsultation = models.CharField(max_length=100)
    correctDateOfEConsultation = models.BooleanField()
    isProblemResolved = models.BooleanField()
    wasVisitProposed = models.BooleanField()
    wereInstructionsClear = models.BooleanField()
    wasDoctorEngaged = models.CharField(max_length=100)
    purposeOfEConsultation = models.CharField(max_length=100)
    useOfETechniques = models.BooleanField()
    isPreparedBeforeEConsultation = models.BooleanField()
    fearOfViolatingConfidentiality = models.CharField(max_length=100)


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    respondentID = models.OneToOneField(General, on_delete=models.CASCADE,
                                        editable=False)  # powiazanie z tabela general za pomoca respondentID
    sessionKey = models.CharField(max_length=100, editable=False)
    yearsOfExperience = models.IntegerField()
    specialization = models.CharField(max_length=100)
    numberOfEConsults = models.IntegerField()
    numberOfVisits = models.IntegerField()
    lengthOfEConsults = models.IntegerField()
    lengthOfVisits = models.IntegerField()
    howManyEConsultsNeedingVisits = models.IntegerField()
    technicalSkillsRating = models.IntegerField()
    arePatientsPrepared = models.BooleanField()
    howManyPatientsDontAnswer = models.IntegerField()
    seriousnessOfPatients = models.CharField(max_length=100)
    cancellingIfNoContact = models.BooleanField()
    limitedTrust = models.BooleanField()
    eTechniquesAndTimeEfficiency = models.BooleanField()
    eTechniquesAndWorkEase = models.BooleanField()
    fearOfReturning = models.CharField(max_length=100)


class AllGroups(models.Model):
    id = models.AutoField(primary_key=True)
    respondentID = models.OneToOneField(General, on_delete=models.CASCADE,
                                        editable=False)  # powiazanie z tabela general za pomoca respondentID
    sessionKey = models.CharField(max_length=100, editable=False)
    didTechnicalProblemsOccur = models.BooleanField()
    eConsultationVsVisit = models.CharField(max_length=100)
    eConsultationAsStandard = models.CharField(max_length=100)
    accessibilityVsLimitingEConsults = models.CharField(max_length=100)
    eConsultationVsChildren = models.CharField(max_length=100)
    queuesAndVisits = models.CharField(max_length=100)
    whoDecidesWhichForm = models.CharField(max_length=100)
    comments = models.TextField()

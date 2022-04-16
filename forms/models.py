from django.db import models


class General(models.Model):
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    residence = models.CharField(max_length=100)
    whoIsRespondent = models.CharField(max_length=100)


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    respondentID = models.OneToOneField(General, on_delete=models.CASCADE)
    usePOZ = models.BooleanField()
    freqOfVisits = models.CharField(max_length=100)
    isPunctual = models.BooleanField()
    correctDateOfEConsultation = models.BooleanField()
    isProblemResolved = models.BooleanField()
    wasVisitProposed = models.BooleanField()
    wereInstructionsClear = models.BooleanField()
    purposeOfEConsultation = models.CharField(max_length=100)
    useOfETechniques = models.BooleanField()
    isPreparedBeforeEConsultation = models.BooleanField()


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    respondentID = models.OneToOneField(General, on_delete=models.CASCADE)
    numberOfEConsults = models.IntegerField()
    numberOfVisits = models.IntegerField()
    technicalSkillsRating = models.IntegerField()
    howManyEConsultsNeedingVisits = models.IntegerField()
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
    respondentID = models.OneToOneField(General, on_delete=models.CASCADE)
    didTechnicalProblemsOccur = models.BooleanField()
    eConsultationVsVisit = models.CharField(max_length=100)
    eConsultationAsStandard = models.CharField(max_length=100)
    accessibilityVsLimitingEConsults = models.CharField(max_length=100)
    eConsultationVsChildren = models.CharField(max_length=100)
    queuesAndVisits = models.CharField(max_length=100)
    whoDecidesWhichForm = models.CharField(max_length=100)
    comments = models.TextField()

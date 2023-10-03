from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    max_appointments = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    patient_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient_name}'s Appointment with Dr. {self.doctor}"

# tracker/models.py

from django.db import models

class EmissionData(models.Model):
    # Define fields for the table
    date = models.DateField()
    kwh_usage = models.FloatField()  # kWh of electricity used
    ng_usage = models.FloatField()   # m³ of natural gas used
    gasoline_usage = models.FloatField()  # Liters of gasoline used
    diesel_usage = models.FloatField()    # Liters of diesel used
    total_emission = models.FloatField()  # Total CO₂ emissions

    def __str__(self):
        return f"Emission data for {self.date}"

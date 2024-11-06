from django import forms

class EnergyUsageForm(forms.Form):
    kwh_usage = forms.FloatField(label="Electricity Usage (kWh)")
    ng_usage = forms.FloatField(label="Natural Gas Usage (m³)")
    gasoline_usage = forms.FloatField(label="Gasoline Usage (liters)")
    diesel_usage = forms.FloatField(label="Diesel Usage (liters)")

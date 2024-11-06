# tracker/views.py
from django.shortcuts import render
from .forms import EnergyUsageForm
from django.shortcuts import render
from tracker.models import EmissionData
import json

def calculate_emissions(request):
    results = {}
    if request.method == 'POST':
        form = EnergyUsageForm(request.POST)
        if form.is_valid():
            kwh = form.cleaned_data['kwh_usage']
            ng = form.cleaned_data['ng_usage']
            gasoline = form.cleaned_data['gasoline_usage']
            diesel = form.cleaned_data['diesel_usage']

            # Calculations
            kwh_emission = kwh * 0.92
            ng_emission = ng * 2.75
            gasoline_emission = gasoline * 2.31
            diesel_emission = diesel * 2.68
            total_emission = kwh_emission + ng_emission + gasoline_emission + diesel_emission

            # Prepare results for rendering
            results = {
                'total_emission': round(total_emission, 2),
                'kwh_emission': round(kwh_emission, 2),
                'ng_emission': round(ng_emission, 2),
                'gasoline_emission': round(gasoline_emission, 2),
                'diesel_emission': round(diesel_emission, 2),
                'percentages': {
                    'kwh': round(kwh_emission / total_emission * 100, 2),
                    'ng': round(ng_emission / total_emission * 100, 2),
                    'gasoline': round(gasoline_emission / total_emission * 100, 2),
                    'diesel': round(diesel_emission / total_emission * 100, 2),
                }
            }
    else:
        form = EnergyUsageForm()
        
    return render(request, 'tracker/calculate_emissions.html', {'form': form, 'results': results})


def chartjs_chart(request):
    data = EmissionData.objects.values('date', 'total_emission')
    dates = [entry['date'].strftime("%Y-%m-%d") for entry in data]
    emissions = [entry['total_emission'] for entry in data]

    return render(request, 'tracker/chartjs_chart.html', {
        'dates': json.dumps(dates),
        'values': json.dumps(emissions)
    })
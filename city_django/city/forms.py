from django import forms


class CityForm(forms.Form):
    address = forms.CharField()
    distance = forms.IntegerField()
    geo_lat = forms.FloatField()
    geo_lon = forms.FloatField()
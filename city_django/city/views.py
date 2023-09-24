import yandex_geocoder
from decouple import config
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.shortcuts import render
from yandex_geocoder import Client
from .forms import CityForm
from .models import City


def geo_coding(address):
    try:
        yandex_geocoder_secret_key = config('YANDEX_GEOCODER_SECRET_KEY')
        client = Client(yandex_geocoder_secret_key)
        coordinates = client.coordinates(address)
        return coordinates
    except yandex_geocoder.exceptions.NothingFound:
        return "Введенный адрес не найден"


def dadata_geocoding(request):
    if request.method == 'GET':
        return render(request, 'city/DaDataGeoCoding.html',
                      {'check_action': "get_req", 'geo_lon': 0, 'geo_lat': 0})
    else:
        form = CityForm(request.POST)
        if form.data['address'] != "" and form.data['distance'] != "":
            result = geo_coding(form.data['address'])
            if type(result) is tuple:
                geo_lat = result[1]
                geo_lon = result[0]
                city_list = []
                radius = form.data['distance']
                point = Point(float(geo_lon), float(geo_lat), srid=4326)
                nearest_city = City.objects.filter(geom__distance_lt=(point, Distance(km=radius)))
                for i in nearest_city:
                    data = [i.geom.x, i.geom.y, i.country, i.federal_district, i.region, i.city, i.foundation_year]
                    city_list.append(data)
                return render(request, 'city/DaDataGeoCoding.html',
                              {'check_action': "points", 'coordinate_list': city_list,
                               'geo_lon': geo_lon, 'geo_lat': geo_lat})
            else:
                return render(request, 'city/DaDataGeoCoding.html',
                              {'check_action': "get_req", 'geo_lon': 0, 'geo_lat': 0, 'error': result})
        elif form.data['address'] != "":
            result = geo_coding(form.data['address'])
            if type(result) is tuple:
                geo_lat = result[1]
                geo_lon = result[0]
                if geo_lon is None or geo_lat is None:
                    return render(request, 'city/DaDataGeoCoding.html')
                else:
                    return render(request, 'city/DaDataGeoCoding.html',
                                  {'check_action': "dadata", 'geo_lon': geo_lon, 'geo_lat': geo_lat})
            else:
                return render(request, 'city/DaDataGeoCoding.html',
                              {'check_action': "get_req", 'geo_lon': 0, 'geo_lat': 0, 'error': result})
        else:
            return render(request, 'city/DaDataGeoCoding.html',
                          {'check_action': "get_req", 'geo_lon': 0, 'geo_lat': 0})

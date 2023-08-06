from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.shortcuts import redirect, render
from .forms import CityForm
from dadata import Dadata
from .models import City

geo_lat = 0
geo_lon = 0


def dadata_geocoding(request):
    global geo_lat
    global geo_lon
    if request.method == 'GET':
        return render(request, 'city/map.html')
    else:
        form = CityForm(request.POST)
        if 'address' in form.data:
            address = form.data['address']
            token = "3cedaba82c441a2534982feaa9d3bec897cba648"
            secret = "b7fe5de3e1e877f310bd21c02cabd5ba81dea71d"
            dadata = Dadata(token, secret)
            result = dadata.clean("address", address)
            geo_lat = result["geo_lat"]
            geo_lon = result["geo_lon"]
            if geo_lon is None or geo_lat is None:
                return render(request, 'city/map.html')
            else:
                return render(request, 'city/DaDataGeoCoding.html', {'geo_lon': geo_lon, 'geo_lat': geo_lat})
        elif 'distance' in form.data:
            city_list = []
            radius = form.data['distance']
            point = Point(float(geo_lon), float(geo_lat), srid=4326)
            nearest_city = City.objects.filter(geom__distance_lt=(point, Distance(km=radius)))
            for i in nearest_city:
                coords = [i.geom.x, i.geom.y]
                city_list.append(coords)
            return render(request, 'city/Citys.html', {'coordinate_list': city_list})
        else:
            return render(request, 'city/map.html')

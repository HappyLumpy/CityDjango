import csv

from django.contrib.gis.geos import fromstr
from django.core.management import BaseCommand
from django.contrib.gis.geos import Point
from city.models import City


class Command(BaseCommand):
    help = 'Add point in DB from Json'

    def handle(self, *args, **options):
        file = open("static/city.csv")
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        for r in rows[1:]:
            city = City(
                address=r[0],
                postal_code=r[1],
                country=r[2],
                federal_district=r[3],
                region_type=r[4],
                region=r[5],
                area_type=r[6],
                area=r[7],
                city_type=r[8],
                city=r[9],
                settlement_type=r[10],
                settlement=r[11],
                kladr_id=r[12],
                fias_id=r[13],
                fias_level=r[14],
                capital_marker=r[15],
                okato=r[16],
                oktmo=r[17],
                tax_office=r[18],
                timezone=r[19],
                geom=Point(float(r[21]), float(r[20])),
                population=r[22],
                foundation_year=r[23]
            )
            city.save()
        file.close()

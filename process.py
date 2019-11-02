import csv
with open('c:/Users/elipp/Desktop/Northeastern University/GIS6345/some.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:  
        print row

import csv
from shapely.geometry import Point
with open('c:/Users/elipp/Desktop/Northeastern University/GIS6345/some.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['lon']), float(row['lat']))

import csv
from shapely.geometry import Point, mapping
from fiona import collection

schema = { 'geometry': 'Point', 'properties': { 'name': 'str' } }
with collection(
    "some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('c:/Users/elipp/Desktop/Northeastern University/GIS6345/some.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['lon']), float(row['lat']))
            output.write({
                'properties': {
                    'name': row['name']
                },
                'geometry': mapping(point)
            })

with collection("some.shp", "r") as input:
    for point in input:
        print shape(point['geometry'])

from shapely.geometry import mapping, shape
from fiona import collection

with collection("some.shp", "r") as input:
    schema = { 'geometry': 'Polygon', 'properties': { 'name': 'str' } }
    with collection(
        "some_buffer.shp", "w", "ESRI Shapefile", schema) as output:
        for point in input:
            output.write({
                'properties': {
                    'name': point['properties']['name']
                },
                'geometry': mapping(shape(point['geometry']).buffer(5.0))
            })

from shapely.geometry import mapping, shape
from shapely.ops import cascaded_union
from fiona import collection

with collection("some_buffer.shp", "r") as input:
    schema = input.schema.copy()
    with collection(
            "some_union.shp", "w", "ESRI Shapefile", schema) as output:
        shapes = []
        for f in input:
            shapes.append(shape(f['geometry']))
        merged = cascaded_union(shapes)
        output.write({
            'properties': {
                'name': 'Buffer Area'
                },
            'geometry': mapping(merged)
            })


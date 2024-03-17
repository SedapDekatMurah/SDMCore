from django.http import JsonResponse
from django.shortcuts import render
from SDMCore.core.scripts import generate

import json


def post_generate(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        latitude = data['latitude']
        longitude = data['longitude']

        if latitude == None or longitude == None:
            return JsonResponse({'message': "Missing location parameters"})

        # Generate database
        if generate.generate_data(latitude, longitude):
            return JsonResponse({'message': "Successfully generated restaurant data for location {},{}. Thank you!".format(latitude, longitude)})
        else:
            return JsonResponse({'message': "Failed to generate restaurant data!"})

    else:
        return JsonResponse({'message': "API request should be POST type"})


def get_restaurants(request):
    if request.method == "GET":
        latitude = request.GET.get("latitude", None)
        longitude = request.GET.get("longitude", None)

        if not latitude or not longitude:
            return JsonResponse({'message': "Missing location parameters"})

        # TODO Get data from db

        return JsonResponse({'message': "Retrieved data!"})
    else:
        return JsonResponse({'message': "API request should be GET type"})

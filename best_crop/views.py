from django.shortcuts import render
import json
import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return render(request, "best_crop/index.html")


@csrf_exempt
def find_best(request):
    df = pd.read_csv('recomend.csv')
    fruits = df.loc[:, "label"].unique()
    fruit_means = {
    }
    for fruit in fruits:
        fruit_means[fruit] = df[df['label'] == fruit].mean()
    data = json.loads(request.body)
    nitro = data.get("nitro", "")
    phos = data.get("phos", "")
    pot = data.get("pot", "")
    temp = data.get("temp", "")
    hum = data.get("hum", "")
    ph_value = data.get("ph_value", "")
    rainfall = data.get("rainfall", "")
    return JsonResponse(fruit_means)

from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults, PredResultSales
from iris.settings import BASE_DIR
import os



def predict(request):
    print(BASE_DIR)
    return render(request, 'predict.html')

def predict_sales(request):
    return render(request, 'predict_sales.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        bedrooms=float(request.POST.get('bedrooms'))	
        bathrooms=float(request.POST.get('bathrooms'))
        land_size=float(request.POST.get('land_size'))
        furnished=request.POST.get('furnished')
        province=request.POST.get('province')	
        district=request.POST.get('district')	
        sector=request.POST.get('sector')

        data = {
        "Bedrooms":bedrooms,
        "Bathrooms":bathrooms,
        "Land size": land_size,
        "Furnished":furnished,
        "Province":	province,
        "District":	district,
        "Sector":	sector,
        }
        df = pd.DataFrame(data, index=[0])
        # Unpickle model
        model = pd.read_pickle(os.path.join(BASE_DIR, "rent_model.pickle"))
        # result = model.predict([[bedrooms, bathrooms, land_size, furnished, province, district, sector]])
        result = model.predict(df)

        classification = result[0]
        PredResults.objects.create(bedrooms=bedrooms, bathrooms=bathrooms, land_size=land_size, furnished=furnished, province=province, district=district, sector=sector, prediction=classification)
        return JsonResponse({'result': classification.item(), 'bedrooms': bedrooms,
                             'bathrooms': bathrooms, 'land_size': land_size, 'furnished': furnished, 'province':province, 'district':district, 'sector':sector},
                            safe=False)




def predict_chance_sales(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        property_type=request.POST.get('property_type')
        bathrooms=float(request.POST.get('bathrooms'))
        bedrooms=float(request.POST.get('bedrooms'))	
        # furnished=request.POST.get('furnished')
        province=request.POST.get('province')	
        district=request.POST.get('district')	
        sector=request.POST.get('sector')
        area=float(request.POST.get('area'))
        data = {
        "property_type":property_type,
        "bathrooms":bathrooms,
        "bedrooms":bedrooms,
        # "Furnished":furnished,
        "province":	province,
        "district":	district,
        "sector":	sector,
        "area": area
        }
        df = pd.DataFrame(data, index=[0])
        # Unpickle model
        model = pd.read_pickle(os.path.join(BASE_DIR, "sales_model.pickle"))
        result = model.predict(df)
        print(result)
        classification = result[0]
        PredResultSales.objects.create(bedrooms=bedrooms, bathrooms=bathrooms, province=province, district=district, sector=sector,area=area, prediction=classification)

        return JsonResponse({'result': classification.item(), 'bedrooms': bedrooms,
                             'bathrooms': bathrooms, 'province':province, 'district':district, 'sector':sector, 'area':area, 'X-Content-Type-Options':'nosniff', 'Cache-Control':'public, max-age=3600'},
                            safe=False)





def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)

def view_sales_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResultSales.objects.all()}
    return render(request, "result_sales.html", data)

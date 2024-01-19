from django.urls import path
from . import views

app_name = "predict"

urlpatterns = [
    path('', views.predict, name='prediction_page'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('predict_chance_sales/', views.predict_chance_sales, name='submit_sales_prediction'),
    path('predict_sales/', views.predict_sales, name='submit_sales'),
    path('results/', views.view_results, name='results'),
    path('sales_result/', views.view_sales_results, name='sales_result'),
]
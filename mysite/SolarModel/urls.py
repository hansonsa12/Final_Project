from . import views
from django.urls import path

app_name = 'SolarModel'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name="index"),
    path('<int:pk>', views.PlanetDetail.as_view(), name="detail"),
    path('add', views.CreateItem.as_view(), name="create_item"),
]
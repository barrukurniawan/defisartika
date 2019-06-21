"""defisartika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from modulcuaca import views as dashboard

urlpatterns = [
    path('data-cuaca/<path:api_key>/<path:temp_value>/<path:hum_value>/<path:press_value>', dashboard.data_cuaca, name='data-cuaca'),
    path('api-summary/', dashboard.api_summary, name='api-summary'),
    path('api-suhu/', dashboard.api_suhu, name='api-suhu'),
    path('api-temp/', dashboard.api_temp, name='api-temp'),
    path('api-kelembaban/', dashboard.api_kelembaban, name='api-kelembaban'),
    path('api-tekananudara/', dashboard.api_tekananudara, name='api-tekananudara'),
    path('grafik', dashboard.web_grafik, name='grafik'),
    path('home', dashboard.web_home, name='home'),
    path('', dashboard.web_raspi, name='raspi'),
    path('excelsuhu/', dashboard.export_suhu_to_xlsx, name='excelSuhu'),
    path('excelkelembaban/', dashboard.export_kelembaban_to_xlsx, name='excelKelembaban'),
    path('exceltekananudara/', dashboard.export_tekananudara_to_xlsx, name='excelTekananudara'),
]

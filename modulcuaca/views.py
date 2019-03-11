from django.shortcuts import render
from django.utils import timezone
from django.conf import settings
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from .models import TabelSuhu, TabelKelembaban, TabelTekananUdara
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
import json, string

# api_suhu, api_kelembaban, api_tekanan udara are import data from database and convert to JSON
# Kenapa di convert ke JSON, karena kita sedang membuat API, dan API memliki format data JSON atau XML
# Fungsi JSON ? sebagai format untuk pertukaran data
# JSON berfungsi untuk pertukaran data dari awalnya data yg diambil dengan bahasa python, lalu jadi sebuah API, yang kemudian kita parse data Json tsb dari API untuk digunakan di bahasa javascript dalam membuat grafik 

def web_grafik(request):
	return render(request, 'modulcuaca/grafik.html')

def api_temp(request):
    querytemp = TabelSuhu.objects.filter(api_key='DEFISR98')

    listing = []
    for item in querytemp:
	    listing.append({
	            'temp_time'     : item.time,
	            'temp_value' 	: item.nilai_suhu
	        })
    return JsonResponse(listing, safe=False)

def api_suhu(request):
    querytemp = TabelSuhu.objects.filter(api_key='DEFISR98')
    datatemp = querytemp.last()

    listing = []

    listing.append({
            'temp_time'     : datatemp.time,
            'temp_value' 	: datatemp.nilai_suhu
        })
    return JsonResponse(listing, safe=False)

def api_kelembaban(request):
    queryhum = TabelKelembaban.objects.filter(api_key='DEFISR98')
    datahum = queryhum.last()

    listing = []

    listing.append({
            'hum_time'      : datahum.time,
            'hum_value' 	: datahum.nilai_kelembaban
        })
    return JsonResponse(listing, safe=False)

def api_tekananudara(request):
    querypress = TabelTekananUdara.objects.filter(api_key='DEFISR98')
    datapress = querypress.last()

    listing = []

    listing.append({
            'press_time'     : datapress.time,
            'press_value' 	: datapress.nilai_tekananudara
        })
    return JsonResponse(listing, safe=False)

@csrf_exempt
def data_cuaca(request, api_key, temp_value, hum_value, press_value):
	suhu = request.POST.get("temp_value", temp_value)
	kelembaban = request.POST.get("hum_value", hum_value)
	tekananudara = request.POST.get("press_value", press_value)

	data_suhu = TabelSuhu.objects.create(
        api_key = api_key,
        nilai_suhu  = suhu
    )
	data_suhu.save()

	data_kelembaban = TabelKelembaban.objects.create(
        api_key = api_key,
        nilai_kelembaban  = kelembaban
    )
	data_kelembaban.save()

	data_tekananudara = TabelTekananUdara.objects.create(
        api_key = api_key,
        nilai_tekananudara  = tekananudara
    )
	data_tekananudara.save()

	querytemp = TabelSuhu.objects.filter(api_key='DEFISR98')
	queryhum = TabelKelembaban.objects.filter(api_key='DEFISR98')
	querypress = TabelTekananUdara.objects.filter(api_key='DEFISR98')

	datatemp = querytemp.last()
	datahum = queryhum.last()
	datapress = querypress.last()
	mydata = []
	mydata.append({
	        'temp_time'		: datatemp.time,
	        'temp_value' 	: datatemp.nilai_suhu,
	        'hum_time'		: datahum.time,
	        'hum_value'		: datahum.nilai_kelembaban,
	        'press_time'	: datapress.time,
	        'press_value'	: datapress.nilai_tekananudara
	    })
	return JsonResponse(mydata, safe=False)
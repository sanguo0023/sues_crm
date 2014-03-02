#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from main.models import *

# Create your views here.
def index(request):
	return render_to_response('index.html', {})

def show(request):
	goods = Goods.objects.all()
	return render_to_response('show.html', {'goods': goods})

def order(request):
	return render_to_response('order.html', {})

def show_image(request, path):
	image_data = open("static/images/" + path, "rb").read()
	return HttpResponse(image_data, mimetype="image/png")

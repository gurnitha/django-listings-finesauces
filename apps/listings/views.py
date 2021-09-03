# apps/listings/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.listings.models import Category

# Create your views here.

# Homepage views
def product_list(request):
	products = Product.objects.all()
	context = {
		'products': products
	}
	return render(request,'product/list.html', context)


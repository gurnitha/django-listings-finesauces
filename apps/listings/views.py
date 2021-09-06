# apps/listings/views.py

# Django modules
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Locals
from apps.listings.models import Category, Product


# Views:product_list
def product_list(request, category_slug=None):
	categories = Category.objects.all()
	requested_category = None
	products = Product.objects.all()

	if category_slug:
		requested_category = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=requested_category)

	context = {
		'categories': categories,
		'requested_category': requested_category,
		'products': products	
	}	
	
	return render(request,'product/list.html', context)


# Views: Product detail
def product_detail(request, category_slug, product_slug):
	
	category 	= get_object_or_404(Category, slug=category_slug)
	product 	= get_object_or_404(Product, category_id=category.id, slug=product_slug)
	
	context 	= {'product': product}
	
	return render(request, 'product/detail.html', context)


# apps/listings/models.py

# Django modules
from django.db import models
from django.urls import reverse

# Create your models here.

# MODEL:Category
class Category(models.Model):

	name = models.CharField(max_length=100,unique=True)
	slug = models.SlugField(max_length=100,unique=True)

	class Meta:
		ordering = ('-name',)
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse(
			'listings:product_list_by_category', args=[self.slug])


# MODEL:Product
class Product(models.Model):

	category = models.ForeignKey(Category,related_name='products',on_delete = models.CASCADE)
	name = models.CharField(max_length=100,unique=True)
	slug = models.SlugField(max_length=100,unique=True)
	image = models.ImageField(upload_to='products/')
	description = models.TextField()
	shu = models.CharField(max_length=10)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	available = models.BooleanField(default=True)

	class Meta:
		ordering = ('shu',)

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# Create your views here.
from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)

from .models import Product
from .forms import ProductModelForm

class ProductCreateView(CreateView):
	template_name = 'products/product_create.html'
	form_class = ProductModelForm
	queryset = Product.objects.all()  #<blog>/<modelname>_list.html
	# success_url = '/'

	# def form_valid(self, form):
	# 	print(form.cleaned_data)
	# 	return super().form_valid(form)

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Product, id=id_)

	def get_success_url(self):
		return reverse('products:product-list')

class ProductListView(ListView):
	template_name = 'products/product_list.html'
	queryset = Product.objects.all()  #<blog>/<modelname>_list.html

class ProductDetailView(DetailView):
	template_name = 'products/product_detail.html'
	queryset = Product.objects.all()  #<blog>/<modelname>_list.html

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Product, id=id_)

class ProductUpdateView(UpdateView):
	template_name = 'products/product_create.html'
	form_class = ProductModelForm
	queryset = Product.objects.all()  #<blog>/<modelname>_list.html

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Product, id=id_)

	# def form_valid(self, form):
	# 	print(form.cleaned_data)
	# 	return super().form_valid(form)

class ProductDeleteView(DeleteView):
	template_name = 'products/product_delete.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Product, id=id_)

	def get_success_url(self):
		return reverse('products:product-list')
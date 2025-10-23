from django.shortcuts import render
from .models import Brand, Category, Product

# Create your views here.
def index(request):

    products = Product.objects all()
    categorys = Category.objects all()
    brands = Brand.objects all()
    return render(request, "app/index.html", context=context)
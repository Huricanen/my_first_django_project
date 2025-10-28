from django.shortcuts import render
<<<<<<< HEAD
from .models import Product, Brand, Category

def index(request):
=======
from .models import Brand, Category, Product

def index(request):

>>>>>>> 525a4ba (Сделана первая версия МП для ДЗ)
    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    context = {
        "products": products,
        "brands": brands,
<<<<<<< HEAD
        "categories": categories
    }
    return render(request, "app/index.html", context=context)
=======
        "categories": categories,
    }

    return render(request, "app/index.html", context=context)
>>>>>>> 525a4ba (Сделана первая версия МП для ДЗ)

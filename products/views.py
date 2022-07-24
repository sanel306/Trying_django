from django.shortcuts import render

from .form import ProductForm, RawProductForm
from .models import Product

# Create your views here.

def product_create_view(request):
    form =ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form' : form,
    }
    return render(request, "product/product_create.html", context)


# #PURE DJANGO FORM

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)

#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)    
#     context = {
#         "form" : my_form
#     }
#     return render(request, "product/product_create.html", context)






def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title' : obj.title,
        'description' : obj.description,
        'price' : obj.price,
        'summary' : obj.summary
    }

    return render(request, "product/detail.html", context)

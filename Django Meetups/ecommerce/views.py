from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def e_index(response):
    # return HttpResponse('Hello Ecommerce')

    item = [
        {'product': 'Diarymilk Chocolate'},
        {'product': 'Milk'}
    ]
    # should not include 'templates/' because django knows that it is in templates
    return render(response, 'ecommerce/index.html',{
        'show_product': True,
        'item': item
    })  
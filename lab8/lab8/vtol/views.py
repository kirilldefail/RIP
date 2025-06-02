from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Item
from .models import ItemDetail

def items(request):
    template = loader.get_template("vtol/items.html")
    context = {'items': Item.objects.all()}
    return HttpResponse(template.render(context, request))

def item_detail(request, id):
    template = loader.get_template("vtol/detail.html")
    context = {'item': ItemDetail.objects.get(id=id)}
    return HttpResponse(template.render(context, request))

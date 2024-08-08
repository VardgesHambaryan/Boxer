from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Home, Divider, Feature, Feature1, Pricing, Download, Contact

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        home = Home.objects.first() 
        dividers = Divider.objects.all()
        feature = Feature.objects.first()
        feature1 = Feature1.objects.first()
        pricings = Pricing.objects.all()
        downloads = Download.objects.first()
        contacts = Contact.objects.first()
        
        context = {
            'home':home,
            'dividers':dividers,
            'feature':feature,
            'feature1':feature1,
            'pricings':pricings,
            'downloads':downloads,
            'contacts':contacts,
        }
        return render(request, self.template_name, context=context)
    
    






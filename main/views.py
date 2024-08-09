from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Home, Divider, Feature, PricingPlan, Download, ContactUs
from .forms import ContactForm


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        home = Home.objects.first()
        dividers = Divider.objects.all()
        featers = Feature.objects.all()
        pricings = PricingPlan.objects.all()
        download = Download.objects.first()
        contacts = ContactUs.objects.first()

        context = {
            'home':home,
            'dividers':dividers,
            'featers':featers,
            'pricings':pricings,
            'download':download,
            'contacts':contacts,
        }
        return render(request, self.template_name, context=context)
    

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            form = ContactForm()

        return redirect('/')
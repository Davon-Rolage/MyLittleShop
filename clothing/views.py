from django.shortcuts import render
from django.views.generic import View, ListView
from .models import PriceList, MyStorage, PartnerStorage, Partner, Sale


class IndexView(View):
    template_name = 'clothing/index.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutView(View):
    template_name = 'clothing/about.html'
    
    def get(self, request):
        return render(request, self.template_name)


class PricelistListView(ListView):
    template_name = 'clothing/pricelist.html'
    model = PriceList
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')

class MyStorageListView(ListView):
    template_name = 'clothing/my_storage.html'
    model = MyStorage
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')

class PartnersStoragesListView(ListView):
    template_name = 'clothing/partners_storages.html'
    model = PartnerStorage

    def get_queryset(self):
        return self.model.objects.all().order_by('-updated_at')

class PartnerListView(ListView):
    template_name = 'clothing/partners.html'
    model = Partner
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')
    

class SalesListView(ListView):
    template_name = 'clothing/sales.html'
    model = Sale

    def get_queryset(self):
        return self.model.objects.all().order_by('-date')



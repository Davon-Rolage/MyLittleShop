from django.urls import path
from .views import IndexView, AboutView, PricelistListView, MyStorageListView, PartnersStoragesListView, PartnerListView, SalesListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('pricelist/', PricelistListView.as_view(), name='pricelist'),
    path('my-storage/', MyStorageListView.as_view(), name='my_storage'),
    path('partners-storages/', PartnersStoragesListView.as_view(), name='partners_storages'),
    path('partners/', PartnerListView.as_view(), name='partners'),
    path('sales/', SalesListView.as_view(), name='sales'),
]

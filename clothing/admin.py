from django.contrib import admin
from import_export.admin import ExportActionMixin

from .models import *


class PriceListAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'price', 'added_at']
    list_filter = ['item_name', 'price']    
    
    
class MyStorageAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'item_count']
    
    
class PartnerStorageAdmin(admin.ModelAdmin):
    list_display = ['partner', 'item', 'count', 'updated_at']
    list_filter = ['partner', 'item', 'updated_at']
    readonly_fields = ['updated_at']
    
class SaleAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['date', 'partner', 'item', 'count', 'total_sales']
    list_filter = ['partner', 'item', 'date']
    readonly_fields = ['total_sales']
    
class PartnerAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display  = ['partner_name', 'address', 'telephone_number', 'website', 'notes', 'added_at']


admin.site.register(PriceList, PriceListAdmin)
admin.site.register(MyStorage, MyStorageAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerStorage, PartnerStorageAdmin)
admin.site.register(Sale, SaleAdmin)

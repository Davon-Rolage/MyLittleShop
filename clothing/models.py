from datetime import datetime
from django.db import models


class PriceList(models.Model):
    
    class Meta:
        verbose_name = 'Price List'
        verbose_name_plural = 'Price List'
    
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.item_name
    
class MyStorage(models.Model):
    class Meta:
        verbose_name = 'My Storage'
        verbose_name_plural = 'My Storage'
    
    item_name = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    item_count = models.PositiveIntegerField()
    
    def __str__(self):
        return f'(my rem. {self.item_count}) - {self.item_name}'
    

class Partner(models.Model):
    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
    
    partner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    telephone_number = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.partner_name


class PartnerStorage(models.Model):
    class Meta:
        verbose_name = 'Partner Storage'
        verbose_name_plural = "Partners' Storages"
        ordering = ('-pk', )
    
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    item = models.ForeignKey(MyStorage, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    updated_at = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return f"(rem. {self.count}) - {self.item.item_name} - {self.partner}"

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        my_storage_item = self.item
        my_storage_item.item_count -= self.count
        my_storage_item.save()
        super().save(*args, **kwargs)
        

class Sale(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(PartnerStorage, on_delete=models.DO_NOTHING)
    count = models.PositiveIntegerField()
    
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.partner.partner_name} - {self.item.item} - {self.count} - {self.date}"
    
    def save(self, *args, **kwargs):
        self.total_sales = self.count * self.item.item.item_name.price
        partner_item = self.item
        partner_item.count -= self.count
        partner_item.save()
        super().save(*args, **kwargs)
    
    def max_count(self):
        return MyStorage.objects.filter(item_name=self.item).aggregate(models.Max('item_count'))['item_count__max']
    
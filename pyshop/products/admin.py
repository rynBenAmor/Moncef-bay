from django.contrib import admin
from .models import Product,Offer
# Register your models here.
#ririadmin 1..9

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
class OfferAdmin(admin.ModelAdmin):
    list_display=("code","discount","description")

admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
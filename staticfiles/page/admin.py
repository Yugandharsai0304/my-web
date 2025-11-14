from django.contrib import admin
from .models import *

# Register your models here.
class listAdmin(admin.ModelAdmin):
    list_display=['img','name']
class delightsAdmin(admin.ModelAdmin):
    list_display=['img','name','price']
class popsiclesAdmin(admin.ModelAdmin):
    list_display=['img','name','price']
class cheeseAdmin(admin.ModelAdmin):
    list_display=['img','name','price']

admin.site.register(list,listAdmin)
admin.site.register(delights,listAdmin)
admin.site.register(popsicles,listAdmin)
admin.site.register(cheese,listAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display=['pid','cid','name','image','badge','rating','price']
class ice_libraryAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(ice_library,ice_libraryAdmin)
admin.site.register(Product,ProductAdmin)
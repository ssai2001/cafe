from django.contrib import admin
from . models import Cuisine,Food,Order

# Register your models here.

# To change the display in admin panel define a class as shown below and register it with the model
class CuisineAdmin(admin.ModelAdmin):
    # To display two all columns;
    list_display = ('category','created_at')
    # To add a search-box;
    search_fields = ('category', )
    # To keep an order
    ordering = ('-category', )

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    search_fields = ('name', )
    list_editable = ('is_available', )
    list_filter = ('is_available', )
    ordering = ('name', )

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_details', 'total_price', 'is_ready', 'is_delivered', 'created_at', 'updated_at')
    list_editable = ('is_ready','is_delivered')
    ordering = ('-id',)

# Register the Cuisine table
admin.site.register(Cuisine, CuisineAdmin)
# Register the Food table
admin.site.register(Food, FoodAdmin)

admin.site.register(Order,OrderAdmin)
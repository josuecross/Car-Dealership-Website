from django.contrib import admin
from .models import CarModel, CarMake

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ['date']
    search_fields = ['name']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name']
    search_fields = ['name', 'description']

# Register models here

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)

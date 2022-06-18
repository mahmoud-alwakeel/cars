from django.contrib import admin
from cars.models import Car

# Register your models here.

# to customise the admnistration form with alot more details
class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Car Information',{'fields':['brand']}),
        ('Time Information',{'fields':['year']}),

    ]

# registered car model to appear in the admnistration view
admin.site.register(Car,CarAdmin)



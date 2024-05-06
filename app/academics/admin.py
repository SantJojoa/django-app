from django.contrib import admin

# Register your models here.
from .models import users,students,identification_types,countries,departments,cities,persons

admin.site.register(users)
admin.site.register(students)
admin.site.register(identification_types)
admin.site.register(countries)
admin.site.register(departments)
admin.site.register(cities)
admin.site.register(persons)
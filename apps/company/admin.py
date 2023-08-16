from django.contrib import admin
from apps.company.models import Product, Company, Review, Profile

admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Profile)

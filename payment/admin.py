from django.contrib import admin
from .models import (
   Arear, 
    Payment, 
    Fee
    )

admin.site.register(Fee)
admin.site.register(Arear)
admin.site.register(Payment)

from django.contrib import admin
from . models import (
     Circumstance,
     Student,
     Assesement,
)

admin.site.register(Circumstance)
admin.site.register(Student)
admin.site.register(Assesement)

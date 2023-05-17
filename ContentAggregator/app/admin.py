from django.contrib import admin
from .models import ProgContent
from .models import HiringContent
from .models import PyContent
from .models import CovidContent
 
# Register your models here.
admin.site.register(ProgContent)
admin.site.register(HiringContent)
admin.site.register(PyContent)
admin.site.register(CovidContent)

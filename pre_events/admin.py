from django.contrib import admin
from .models import PreEvent
# Register your models here.


class PreEventAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(PreEvent, PreEventAdmin)

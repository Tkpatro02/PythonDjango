from django.contrib import admin
from .models import Chaivarity,chaiReview,chaiCertificate,Store
# Register your models here.

class chaiReviewInLine(admin.TabularInline):
    model=chaiReview
    extra=2

class chaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type')
    inlines=[chaiReviewInLine]


class storeAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('chai_varities',)

class certificateAmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')








admin.site.register(Chaivarity,chaiVarietyAdmin)
admin.site.register(Store,storeAdmin)
admin.site.register(chaiCertificate,certificateAmin)
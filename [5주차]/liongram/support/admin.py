from django.contrib import admin

from support.models import Faq, Inquiry

# Register your models here.

@admin.register(Inquiry)
class InqueryModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    pass



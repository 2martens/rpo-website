from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from rpocore.models import SupportGroup, SupporterPage, NotableSupporter

admin.site.register(SupportGroup)
admin.site.register(SupporterPage, PageAdmin)
admin.site.register(NotableSupporter)

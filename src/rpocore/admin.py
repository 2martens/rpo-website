from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from rpocore.models import *

admin.site.register(SupportGroup)
admin.site.register(SupporterPage, PageAdmin)
admin.site.register(NotableSupporter)
admin.site.register(FormalStatement)
admin.site.register(InformalStatement)
admin.site.register(StatementPage, PageAdmin)

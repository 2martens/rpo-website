from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from rpocore.models import SupportGroup, SupporterPage, NotableSupporter, Statement, StatementPage

admin.site.register(SupportGroup)
admin.site.register(SupporterPage, PageAdmin)
admin.site.register(NotableSupporter)
admin.site.register(Statement)
admin.site.register(StatementPage, PageAdmin)

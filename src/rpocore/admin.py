from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin, StackedDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

from rpocore.models import *


class PhaseInline(TabularDynamicInlineAdmin):
    model = Phase


class ProcessAdmin(admin.ModelAdmin):
    inlines = [
        PhaseInline,
    ]


class CarouselItemInline(StackedDynamicInlineAdmin):
    model = CarouselItem


class HomepagePageAdmin(PageAdmin):
    inlines = [
        CarouselItemInline,
    ]


class NotableSupporterInline(StackedDynamicInlineAdmin):
    model = NotableSupporter


class SupporterPageAdmin(PageAdmin):
    inlines = [
        NotableSupporterInline,
    ]

admin.site.register(SupportGroup)
admin.site.register(SupporterPage, SupporterPageAdmin)
admin.site.register(NotableSupporter)
admin.site.register(FormalStatement)
admin.site.register(InformalStatement)
admin.site.register(StatementPage, PageAdmin)
admin.site.register(Phase)
admin.site.register(Process, ProcessAdmin)
admin.site.register(CarouselItem)
admin.site.register(HomepagePage, HomepagePageAdmin)

from adminsortable2.admin import SortableAdminMixin
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

    class Media:
        css = {
            "all": ("campaign.css",)
        }


class CarouselAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


class EventAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


class SupportingOrganizationAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(SupportGroup)
admin.site.register(SupporterPage, SupporterPageAdmin)
admin.site.register(NotableSupporter)
admin.site.register(FormalStatement)
admin.site.register(InformalStatement)
admin.site.register(StatementPage, PageAdmin)
admin.site.register(Phase)
admin.site.register(Process, ProcessAdmin)
admin.site.register(CarouselItem, CarouselAdmin)
admin.site.register(HomepagePage, HomepagePageAdmin)
admin.site.register(SupportingOrganization, SupportingOrganizationAdmin)
admin.site.register(Event, EventAdmin)

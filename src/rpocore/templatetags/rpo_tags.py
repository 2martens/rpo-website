
from mezzanine import template

from rpocore.models import SupportingOrganization, Event

register = template.Library()


@register.as_tag
def support_orgs(*args):
    return SupportingOrganization.objects.all()


@register.as_tag
def events(*args):
    return Event.objects.all()


from mezzanine import template

from rpocore.models import SupportingOrganization

register = template.Library()


@register.as_tag
def support_orgs(*args):
    return SupportingOrganization.objects.all()

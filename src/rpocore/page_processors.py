from mezzanine.pages.page_processors import processor_for

from rpocore.models import SupporterPage, Supporter


@processor_for(SupporterPage)
def support_statements(request, page):
    supporters = Supporter.objects.select_related('user').all()
    return {'supporters': supporters}

from mezzanine.pages.page_processors import processor_for

from rpocore.models import SupporterPage, Supporter, SupportGroup


@processor_for(SupporterPage)
def support_statements(request, page):
    supporters = Supporter.objects.select_related('user').all()
    return {'supporters': supporters}


@processor_for(SupporterPage)
def support_statistics(request, page):
    all_supporters = Supporter.objects.all()
    uhh_supporters = all_supporters.filter(university='UHH')
    uhh_count = uhh_supporters.count()
    all_count = all_supporters.count()
    other_count = all_count - uhh_count
    support_groups = SupportGroup.objects.all()
    data_by_group = []
    for group in support_groups:
        group_total_count = all_supporters.filter(support_group__name=group.name).count()
        group_uhh_count = uhh_supporters.filter(support_group__name=group.name).count()
        total_amount = group.total_amount
        goals = group.stretch_goals.split(',')
        current_goal = total_amount

        for goal in goals:
            if group_uhh_count < int(goal) <= total_amount:
                current_goal = int(goal)
                break
        current_percentage = "{:.0%}".format(group_uhh_count / current_goal)

        data_by_group.append(
            (group.name, group_total_count, group_uhh_count, total_amount, current_goal, current_percentage)
        )

    return {'uhh_count': uhh_count, 'other_count': other_count, 'all_count': all_count, 'data': data_by_group}

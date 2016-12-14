from datetime import date
from mezzanine.pages.page_processors import processor_for

from rpocore.models import SupporterPage, Supporter, SupportGroup, HomepagePage, Phase, Process


@processor_for(SupporterPage)
def support_statements(request, page):
    supporters = Supporter.objects.select_related('user').all().filter(user__is_active=True)
    return {'supporters': supporters}


@processor_for(SupporterPage)
def support_statistics(request, page):
    all_supporters = Supporter.objects.all().filter(user__is_active=True)
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


@processor_for(HomepagePage)
def progress_data(request, page):
    phases_all = Phase.objects.all()
    phases_used = phases_all.filter(process=page.homepagepage.process)
    phases_successful = phases_used.filter(start_date__lt=date.today()).filter(end_date__lt=date.today())
    phase_count = phases_used.count()
    phase_successful_count = phases_successful.count()
    width_remaining_progress = 1 if phase_successful_count + 1 > phase_count \
        else (phase_successful_count + 1) / phase_count
    phase_data = []
    iterator = 1

    for phase in phases_used:
        division = 1 if iterator == phase_count else iterator / phase_count
        current_percentage = "{:.0%}".format(division) if division != 1 else "1em"
        data = {
            'percentage': current_percentage,
            'phase': phase
        }
        phase_data.append(data)
        iterator += 1

    return {
        'phases': phase_data,
        'process': page.homepagepage.process,
        'amountOfPhases': phase_count,
        'amountSuccessfulPhases': phase_successful_count,
        'activePhaseNumber': phase_successful_count + 1,
        'widthSuccessfulProgress': "{:.0%}".format((phase_successful_count / phase_count) / width_remaining_progress),
        'widthRemainingProgress': "{:.0%}".format(width_remaining_progress)
    }

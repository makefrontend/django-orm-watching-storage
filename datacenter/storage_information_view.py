from datacenter.models import Visit, get_duration, format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    active_visists = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for active_visist in active_visists:
        non_closed_visits.append({
            'who_entered': active_visist.passcard.owner_name,
            'entered_at': localtime(active_visist.entered_at),
            'duration': format_duration(get_duration(active_visist))
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

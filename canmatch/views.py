from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Job, Candidate


def home(request):
    return render(request, 'canmatch/home.html')


def CandidateFinder(request, search):
    jobs = Job.objects.filter(title=search)
    candidates = Candidate.objects.filter(title=search)
    rs = [i for i in jobs.values_list('skills', flat=True)]
    required_skills = jobs.values_list('skills', flat=True).distinct()
    candidates = candidates.filter(skills__in=required_skills).distinct()
    # candidates = candidates.values()
    # print(candidates.values())
    context = {
        'rs': rs,
        "jobs": jobs,
        "search": search,
        'candidates': candidates,

    }

    return render(request, 'canmatch/match.html', context)

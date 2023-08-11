from django.shortcuts import render, get_object_or_404
from .models import JobPosting


# Create your views here.
def index(request):
    jobs = JobPosting.objects.all()
    active_jobs = JobPosting.objects.filter(is_active=True)
    print(jobs)
    print(active_jobs)
    context = {
        'job_postings': active_jobs,
    }
    return render(request, "job_board/index.html", context)


def job_detail(request, job_id):
    # job = JobPosting.objects.get(id=job_id)
    job = get_object_or_404(JobPosting, id=job_id, is_active = True)
    context = {
        'job': job,
    }
    return render(request, "job_board/job_detail.html", context)

from django.shortcuts import render
from . import models
from django.views import generic


# Create your views here.
def index(request):
    subs = models.Submission.objects.all()
    return render(request, 'index.html', {
        'subs': subs
    })

class SubmissionList(generic.ListView): 
    model = models.Submission
    context_object_name = "submissions"

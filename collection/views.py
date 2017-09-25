from django.shortcuts import render
from collection.models import Submission

# Create your views here.
def index(request):
    subs = Submission.objects.all()
    return render(request, 'index.html', {
        'subs': subs
    })

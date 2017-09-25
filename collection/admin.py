from django.contrib import admin
from collection.models import Submission

class SubmissionAdmin(admin.ModelAdmin):
    model = Submission
    list_display = ('title', 'score', 'url')


# Register your models here.
admin.site.register(Submission, SubmissionAdmin)

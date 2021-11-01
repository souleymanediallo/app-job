from django import forms
from .models import Job


class JobFormCreate(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", "category", "company", "job_type", "location", "description"]

    def __init__(self, *args, **kwargs):
        super(JobFormCreate, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})

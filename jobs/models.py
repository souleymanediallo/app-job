from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def job_count(self):
        return self.jobs.all().count() * 400


class Job(models.Model):
    TYPE_CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
        ('temporary', 'Temporary'),
    )
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="jobs")
    company = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default=None)
    location = models.CharField(max_length=200, blank=False, default=None)
    description = RichTextField(blank=False, default=None)
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    employee = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, blank=True, related_name="job_employee")
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)



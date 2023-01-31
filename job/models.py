from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    date_posted = models.DateTimeField(verbose_name='date posted', auto_now_add=True)
    featured = models.BooleanField(default=False)
    job_category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.job_title

class Category(models.Model):
    job_category = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.job_category
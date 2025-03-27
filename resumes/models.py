from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    skills = models.TextField()
    experience = models.TextField()
    job_match_score = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


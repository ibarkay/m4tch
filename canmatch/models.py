from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=120, default="anon")
    title = models.CharField(max_length=120)  # max_length = required
    skills = models.ManyToManyField(to='Skill', blank=True, default=None)

    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    skills = models.ManyToManyField(to='Skill', blank=True, default=None)

    def __str__(self):
        return self.title



class Skill(models.Model):
    skills = models.CharField(max_length=120, default='css,html')

    def __str__(self):
        return self.skills
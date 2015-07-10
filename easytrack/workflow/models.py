from django.db import models
from contacts.models import Contact

class Project(models.Model):
    pass


class Workflow(models.Model):
    title = models.CharField(max_length=100)

    def on_completion(self):
        pass


class Stage(models.Model):
    title = models.CharField(max_length=100)

    def on_enter(self):
        pass

    def on_exit(self):
        pass

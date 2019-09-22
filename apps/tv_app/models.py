from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData, id):
        errors = {}
        rel_date = datetime.strptime(postData['release'], "%Y-%m-%d")
        if len(postData['title']) < 2:
            errors['name'] = "Title should be at least 2 characters."
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters."
        if rel_date > datetime.now():
            errors['release_date'] = "Cannot have future release date!"
        if (len(postData['description']) > 0) and (len(postData['description'])) < 10:
            errors['description'] = "Description must be at least 10 characters."
        if not id is None:
            if (self.filter(title = postData['title']).exclude(id = id).exists()):
                errors['duplicate'] = "Title already exists."
        else:
            if (self.filter(title = postData['title']).exists()):
                errors['duplicate'] = "Title already exists."
        return errors

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255, null = True)
    release_date = models.DateTimeField(null = True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()

    def __repr__(self):
        return f"{self.title}, Network: {self.network}. Released {self.release_date}."
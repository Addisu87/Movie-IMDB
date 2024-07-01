import os
import uuid

from django.db import models

from core.abstract.models import AbstractModel


def actor_image(filename):
    """
    Generate file path for new actor profile image.
    """
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'
    return os.path.join('actor', filename)


class Actor(AbstractModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.ImageField(blank=True, upload_to=actor_image)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

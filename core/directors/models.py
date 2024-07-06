import os
import uuid
from django.db import models
from core.abstract.models import AbstractModel


def director_image_path(instance, filename):
    """
    Generate file path for new director profile image.
    """
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'
    return os.path.join('directors', filename)


class Director(AbstractModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    director_photo = models.ImageField(
        null=True, upload_to=director_image_path)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

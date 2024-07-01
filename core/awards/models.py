
from django.db import models

from core.actors.models import Actor
from core.abstract.models import AbstractModel


class Award(AbstractModel):
    actor = models.ForeignKey(
        Actor, related_name='award', on_delete=models.CASCADE)
    award_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.award_name}"

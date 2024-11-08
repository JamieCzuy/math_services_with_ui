import copy

from django.db import models
from django.db.models import UniqueConstraint
from django.utils import timezone


# Create your models here.
class SquaresDifference(models.Model):

    given_number = models.PositiveIntegerField()
    value = models.PositiveIntegerField()
    occurrences = models.PositiveIntegerField()
    last_requested = models.DateTimeField(blank=True, null=True)

class Triplet(models.Model):

    a = models.PositiveIntegerField()
    b = models.PositiveIntegerField()
    c = models.PositiveIntegerField()
    product = models.PositiveIntegerField()
    is_triplet = models.BooleanField()
    occurrences = models.PositiveIntegerField(default=0)
    last_requested = models.DateTimeField(blank=True, null=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['a', 'b', 'c'], name='unique_a_b_c')
        ]

    @classmethod
    def get_or_create(cls, a: int, b: int, c: int):
        instance = cls.objects.filter(a=a, b=b, c=c).first()
        if not instance:
            product = a * b * c
            is_triplet = a * a + b * b == c * c
            instance = cls(
                a=a,
                b=b,
                c=c,
                product=product,
                is_triplet=is_triplet,
                occurrences=0,
                last_requested=None,
            )
        as_of_instance = copy.copy(instance)
        instance.occurrences += 1
        instance.last_requested=timezone.now()
        instance.save()
        return as_of_instance

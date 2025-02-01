from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    translator = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=100)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                               default=0, help_text="0 to 5")
    year = models.IntegerField()
    pages = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Book'


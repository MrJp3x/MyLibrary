from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    translator = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    pages = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Book'

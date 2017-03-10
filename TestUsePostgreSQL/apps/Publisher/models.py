from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100, blank=False, help_text='The length is no more than 100 characters.')
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'test_publisher'
        verbose_name = 'Publisher'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


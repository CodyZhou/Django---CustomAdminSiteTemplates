from django.db import models

from TestUsePostgreSQL.apps.Author.models import Author
from TestUsePostgreSQL.apps.Publisher.models import Publisher
from TestUsePostgreSQL.libs.choices import BOOK_STATUS_CHOICE


# Create your models here.
class Book(models.Model):
    author = models.ManyToManyField(Author, blank=False)
    publisher = models.ForeignKey(Publisher, blank=False)
    title = models.CharField(max_length=100, blank=False, help_text='The length is no more than 100 characters.')
    summary = models.TextField(max_length=300, blank=True, help_text='The length is no more than 300 characters.')
    status = models.PositiveSmallIntegerField(choices=BOOK_STATUS_CHOICE, default=0)
    publish_date = models.DateField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'test_book'
        verbose_name = 'Book'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


from django.db import models

from TestUsePostgreSQL.apps.Author.models import Author

# Create your models here.
# Test for change this file.
# Got this message!!
# This is a test for .gitignore file.

# Book Statuses
BOOK_STATUS_CHOICES = (
    (0, 'Arrived'),
    (10, 'New Book For Sale'),
    (15, 'For Sale'),
    (20, 'Discount'),
    (30, 'Discontinued'),
    (40, 'Special Offer'),
    (50, 'Sold Out')
)


class Book(models.Model):
    title = models.CharField(max_length=100, help_text='The length is no more than 100 characters.')
    summary = models.TextField(max_length=300, help_text='The length is no more than 300 characters.')
    author = models.ManyToManyField(Author)
    # publisher =
    status = models.PositiveSmallIntegerField(choices=BOOK_STATUS_CHOICES, default=0)
    publish_date = models.DateField()
    added_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'test_book'

    def __str__(self):
        return self.title


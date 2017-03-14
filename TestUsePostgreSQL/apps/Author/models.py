from django.db import models

from TestUsePostgreSQL.libs.choices import AUTHOR_STATUS_CHOICE

from TestUsePostgreSQL.apps.Localisation.models import Country, Zone


# Author Model
class Author(models.Model):
    """
        Model Name: Author
        Relationship:
            One to Many with AuthorAddress model,
            Many to Many with Book model,
        Description:
            Used to save the author's information.
    """
    firstname = models.CharField(max_length=50, help_text='This length is no more than 50 characters.')
    lastname = models.CharField(max_length=50, help_text='This length is no more than 50 characters.')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.PositiveSmallIntegerField(choices=AUTHOR_STATUS_CHOICE, default=0)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'test_author'
        verbose_name = 'Author'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0} {1}' . format(self.firstname, self.lastname)


# Author's Address Model
class AuthorAddress(models.Model):
    """
        Model Name: AuthorAddress.
        Relationship:
            Many to one with Author model.
        Description:
            Used to save the author's address information. An author can have many addresses.
    """
    author = models.ForeignKey(Author, blank=False, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=50, blank=False, help_text='This length is no more than 50 characters.')
    address_2 = models.CharField(max_length=50, blank=True, help_text='Apt. No., Suite No. and so on.<br>'
                                                          'This length is no more than 50 characters.')
    city = models.CharField(max_length=20, blank=False, help_text='City Name. '
                                                                  'This length is no more than 20 characters.')
    zip = models.CharField(max_length=20, blank=False, help_text='Zipcode.'
                                                                 'This length is no more than 20 characters.')
    zone = models.ForeignKey(Zone)
    country = models.ForeignKey(Country)

    class Meta:
        db_table = 'test_author_address'
        verbose_name = 'Author Address'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author.firstname + ' ' + self.author.lastname

    def get_address(self):
        result_address = self.address_1 + ', '
        if len(self.address_2) >= 1:
            result_address += self.address_2 + ', '
            pass
        result_address += self.city + ', '
        result_address += self.zone.code + ' '
        result_address += self.zip + ', '
        # result_address += [choice[1] for choice in COUNTRY_CHOICE if choice[0] == self.country][0]
        result_address += self.country.iso_code_3

        return result_address


from django.db import models

# Options for author's status
AUTHOR_STATUS_CHOICE = (
    (0, 'New Author'),
    (10, 'Author'),
    (20, 'Retirement')
)


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
    added_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'test_author'

    def __str__(self):
        return '{0} {1}' . format(self.firstname, self.lastname)


# Options for country
COUNTRY_CHOICES = (
    (1, 'Mexico'),
    (10, 'United States'),
    (11, 'Canada'),
    (12, 'United Kingdom'),
    (13, 'China'),
)


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
    address_2 = models.CharField(max_length=50, help_text='Apt. No, Suite No and so on.<br>'
                                                          'This length is no more than 50 characters.')
    city = models.CharField(max_length=20, blank=False, help_text='City Name. '
                                                                  'This length is no more than 20 characters.')
    state = models.CharField(max_length=20, blank=False, help_text='State Name. '
                                                                   'This leng is no more than 20 characters.')
    zip = models.CharField(max_length=20, blank=False, help_text='Zipcode.'
                                                                 'This length is no more than 20 characters.')
    country = models.PositiveSmallIntegerField(choices=COUNTRY_CHOICES, default=10, blank=False)

    class Meta:
        db_table = 'test_author_address'

    def __str__(self):
        return self.author.firstname + ' ' + self.author.lastname

    def get_address(self):
        result_address = self.address_1 + ', '
        if self.address_2 is not None:
            result_address += self.address_2 + ', '
            pass
        result_address += self.city + ', '
        result_address += self.state + ' '
        result_address += self.zip + ', '
        result_address += [choice[1] for choice in COUNTRY_CHOICES if choice[0] == self.country][0]

        return result_address


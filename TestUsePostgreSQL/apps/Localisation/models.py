from django.db import models

from TestUsePostgreSQL.libs.choices import ENABLE_DISABLE_CHOICE


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Country Name',
                            help_text='The length is no more than 100 characters.')
    iso_code_3 = models.CharField(max_length=3, blank=False, verbose_name='Country ISO Code',
                                  help_text='The length is no more than 3 characters.')
    status = models.PositiveSmallIntegerField(verbose_name='Status', default=0, choices=ENABLE_DISABLE_CHOICE)

    class Meta:
        db_table = 'test_country'
        verbose_name = 'Country'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Zone(models.Model):
    country = models.ForeignKey(Country)
    name = models.CharField(max_length=100, blank=False, verbose_name='Zone Name',
                            help_text='The length is no more than 100 characters.')
    code = models.CharField(max_length=3, blank=False, verbose_name='Zone Code',
                                  help_text='The length is no more than 3 characters.')
    status = models.PositiveSmallIntegerField(verbose_name='Status', default=0, choices=ENABLE_DISABLE_CHOICE)

    class Meta:
        db_table = 'test_zone'
        verbose_name = 'Zone'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


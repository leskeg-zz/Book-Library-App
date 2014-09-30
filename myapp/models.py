# Create your models here.

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Book(models.Model):
	title = models.CharField(max_length=100)
	publisher = models.ForeignKey('Publisher')
	year = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(date.today().year)])

	def __unicode__(self):
		return self.title

class Publisher(models.Model):
	fullname = models.CharField(max_length=50)

	def __unicode__(self):
		return self.fullname
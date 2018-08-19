import os
import uuid

from django.db import models
from django.core.validtors import RegexValidator
from django.contrib.auth.models import User


# Create your models here.
class Request(models.Model):
	district = models.CharField(
		max_length = 15, 
		verbose_name = 'District',
		choices = districts,
		)
	location = models.CharField( max_length = 500, verbose_name = 'Location')
	requestee = models.CharField(max_length = 100, verbose_name = 'Requestee')
	requestee_phone = models.CharField(max_length = 10, verbose_name = 'Requestee_phone')
	latlng = models.CharField(max_length = 100, verbose_name = 'GPS-Coordinate - GPS', blank= True)
	latlng_accuracy = models.CharField(max_length = 100, verbose_name = 'GPS-Accuracy', blank=True)

	# If it is enable no need to consider lat and lng

	is_request_for_others = models.BooleanField(verbose_name = 'Requesting for others-', default = False, help_text = 'If it is enabled, no need to consider lat and lng')

	needwater = models.BooleanField(verbose_name = 'Water')
	needfooed = models.BooleanField(verbose_name = 'Food')
	needcloth = models.BooleanField(verbose_name = 'Cloth')
	needmed = models.BooleanField(verbose_name = 'Medicine')
	needtoilet = models.BooleanField(verbose_name = 'Toilet')
	needkit_util = models.BooleanField(verbose_name = 'Kitchen Utilities')
	needrescue = models.BooleanField(verbose_name = 'Rescue')





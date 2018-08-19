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

	detailwater = models.CharField(max_length = 250, verbose_name = 'Detail for required water', blank = True)
	detailfood = models.CharField(max_length = 250, verbose_name = 'Detail for requird food', blank = True)
	detailcloth = models.CharField(max_length = 250, verbose_name = 'Detail for requird cloth', blank = True)
	detailmed = models.CharField(max_length = 250, verbose_name = 'Detail for required medicine', blank = True)
	detailtoilet = models.CharField(max_length = 250, verbose_name = 'Detail for required toilet', blank = True)
	detailkt_utils = models.CharField(max_length = 250, verbose_name = 'Detail for required kitchen utilities', blank = True)
	detailrescue = models.CharField(max_length = 250, verbose_name = 'Detail for required rescue', blank = True)

	needothers = models.CharField(max_length = 500, verbose_name = 'required others', blank = True)

	status = models.CharField(
		max_length = 10,
		choices = status_type,
		default = 'new'
		)
	supply_details = models.CharField(max_length = 10, blank = True)
	dateadd = models.DateTimeField(auto_now_add = True)


	def summarise(self):
		out = " "

		if (self.needwater):
			out += "water requirements :\n {}".format(self.detailwater)
		if (self.needfood):
			out += "food requirements :\n {}".format(self.detailfood)
		if (self.needcloth):
			out += "cloth requirements :\n {}".format(self.detailcloth)
		if (self.needmed):
			out += "medicine requirements :\n {}".format(self.detailmed)
		if (self.needtoilet):
			out += "toilet requirements :\n {}".format(self.detailtoilet)
		if (self.needkit_util):
			out += "Kitchen Utilities requirements :\n {}".format(self.detailkt_utils)
		if (self.needothers.strip() != 0):
			out += "\nOthers needs :\n {}".format(self.needothers)
		
		return out

	class Meta:
		verbose_name = 'Rescue: Request'
		verbose_name_request = 'Rescue : Resquest'

	def __str__(self):
		return self.get_district_display()+' '+self.location






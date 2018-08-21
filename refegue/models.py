import os
import uuid

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


divisions = (
	('dha', 'Dhaka'),
	('Cht', 'Chittagong'),
	('raj', 'Rajshai'),
	('bri', 'Barishal'),
	('khu', 'Khulna'),
	('syh', 'Sylhet'),
	('ran', 'Rangpur'),
	('mym', 'Mymensingh'),
)

districts = (
		('bar', 'Barguna'),
		('bri', 'Barisal'),
		('bhl', 'Bhola'),
		('jhl', 'Jhalokati'),
		('pat', 'Patuakhali'),
		('pir', 'Pirojpur'),
		('ban', 'Bandarban'),
		('bhm', 'Brahmanbaria'),
		('chd', 'Chandpur'),
		('cht', 'Chittagong'),
		('com', 'Comilla'),
		('cox', 'Cox\'s Bazar'),
		('fen', 'Feni'),
		('khg', 'Khagrachhari'),
		('lkh', 'Lakshmipur'),
		('nkh', 'Noakhali'),
		('rgm', 'Rangamati'),
		('dhk', 'Dhaka'),
		('frd', 'Faridpur'),
		('gaz', 'Gazipur'),
		('gop', 'Gopalganj'),
		('kis', 'Kishoreganj'),
		('mad', 'Madaripur'),
		('man', 'Manikganj'),
		('mun', 'Munshiganj'),
		('nar', 'Narayanganj'),
		('nas', 'Narsingdi'),
		('raj', 'Rajbari'),
		('sha', 'Shariatpur'),
		('tan', 'Tangail'),
		('bag', 'Bagerhat'),
		('chu', 'Chuadanga'),
		('jes', 'Jessore'),
		('jhe', 'Jhenaidah'),
		('khu', 'Khulna'),
		('kus', 'Kushtai'),
		('mag', 'Magura'),
		('meh', 'Meherpur'),
		('nri', 'Narail'),
		('sat', 'Satkhira'),
		('jam', 'Jamalpur'),
		('mym', 'Mymensingh'),

	)

status_type = (
	('new', 'New'),
	('pro', 'In progress'),
	('sup', 'Supplied'),
)

vol_categories = (
	('dcr', 'Doctor'),
	('hsv', 'Health Service'),
	('elw', 'Electrical Works'),
	('mew', 'Mechanical Works'),
	('cvw', 'Civil Works'),
	('plw', 'Plumbing works'),
	('vls', 'Vehical support'),
	('ckg', 'Cooking'),
	('rlo', 'relief operation'),
	('cln', 'Cleaning'),
	('bot', 'Boat Service'),
	('rck', 'Rock Climbing'),
	('oth', 'Others'),
)

contrib_status_types = (
	('new', 'New'),
	('ful', 'Fullfilled'),
)

relief_camp_status = (
	('active', 'Activate'),
	('closed', 'Closed'),
)

gender = (
	(0, 'Male'),
	(1, 'Female'),
	(2, 'Others'),
)
# Create your models here.
class Request(models.Model):
	
	division = models.CharField(
		max_length = 10,
		verbose_name = 'Division',
		choices = divisions,
		)

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
		verbose_name_plural = 'Rescue : Resquest'

	def __str__(self):
		return self.get_district_display()+' '+self.location


class Volunteer(models.Model):
	division = models.CharField(
		max_length = 10,
		verbose_name = 'Divisions',
		choices = divisions,
	)

	district = models.CharField(
		max_length = 15,
		verbose_name = 'districts',
		choices = districts,
	)

	name = models.CharField(max_length =100),
	phone = models.CharField(
		max_length = 10,
		verbose_name = 'Phone',
		validators = [RegexValidator(regex='^[6-9]\d{9}$', 
			message = "Please enter 10 digit mobile number", 
			code = 'invalid_mobile')]
	)

	organization = models.CharField(
		max_length = 250,
		verbose_name = 'Organization',
	)

	address = models.TextField(verbose_name = 'address')
	area = models.CharField(
		max_length = 15,
		verbose_name = 'Area of volunteering',
		choices = vol_categories,
	)
	is_spoc=models.BooleanField(default = False, verbose_name = 'Is point of Contact')
	joined = models.DateTimeField(auto_now_add = True)
	is_active = models.BooleanField(default = True)

	class Meta:
		verbose_name = 'Volunteer: individual'
		verbose_name_plural = 'Volunteer: individual'

	def __str__(self):
		return self.name

class NGO(models.Model):
	division = models.CharField(
		max_length = 10,
		verbose_name = 'divisions',
		choices = divisions,
	)
	district = models.CharField(
		max_length = 15, 
		verbose_name = 'districts',
		choices = districts,
	)
	organization = models.CharField(
		max_length = 250,
		verbose_name = 'Name of organization'
	)

	organization_type = models.CharField(max_length = 250, verbose_name = 'Type of Organization')
	organiation_address = models.TextField(default = '', verbose_name = 'Address of organization')
	name = models.CharField(max_length = 100, verbose_name = 'Contact person')
	phone_regex = RegexValidator(
		regex=r'^\+?1?\d{9, 15}$',
		message = 'Phone number must be entered in the format:"+999999999".upto 15 digits ')
	phone = models.CharField(validators=[phone_regex], max_length =17, blank= True)
	description = models.TextField(verbose_name = 'About organization')
	area = models.TextField(verbose_name = 'Area of volunteering')
	location = models.CharField(max_length = 500, verbose_name = 'Preferred location to volunteer')

	is_spoc = models.BooleanField(default = False, verbose_name = 'Is point of Contact')
	joined = models.DateTimeField(auto_now_add= True)

	class Meta:
		verbose_name =  'Volunteer: NGO'
		verbose_name_plural = 'Volunteer: NGOs'

	def __str__(self):
		return self.name


class Contributor(models.Model):
	divison = models.CharField(
		max_length = 10,
		verbose_name = 'Divisions',
		choices = divisions,
	)

	district = models.CharField(
		max_length = 15,
		verbose_name = 'Districts',
		choices = districts,
	)
	name = models.CharField(max_length = 100, verbose_name = 'Name')
	phone = models.CharField(
		max_length = 10, 
		verbose_name = 'Phone -', 
		validators = [RegexValidator(regex='^[6-9]\d{9}$', 
		message = 'Please Enter 10 digit mobile', 
		code = 'invalid_mobile')])
	address = models.TextField(verbose_name = 'Address')
	commodities = models.TextField(verbose_name = 'What you can contributor. (..)')
	status = models.CharField(
		max_length = 10,
		choices = contrib_status_types, 
		default = 'new',
	)

	class Meta:
		verbose_name = 'Contributor:Donation'
		verbose_name_plural = 'Contributors:Donations'

	def __str__(self):
		return self.name + ' '+ self.get_district_display


class DistrictManager(models.Model):
	district = models.CharField(
		max_length = 15,
		verbose_name = 'Districts',
		choices = districts,
	)

	name = models.CharField(max_length = 100, verbose_name = 'Name -')
	phone = models.CharField(max_length =11, verbose_name = 'phone')
	email = models.CharField(max_length =100, verbose_name = 'Email')

	class Meta:
		verbose_name = 'District: Manager'
		verbose_name_plural = 'Districts: Managers'

	def __str__(self):
		return self.name + ' '+self.get_district_display

class DistrictNeed(models.Model):
	district = models.CharField(
		max_length = 15,
		choices = districts,
	)
	needs = models.TextField(verbose_name = 'Item required')
	cnandpts = models.TextField(verbose_name = 'Contacts and collection points')

	class Meta:
		verbose_name = 'District: Need'
		verbose_name_plural = 'Districts: Needs'

	def __str__(self):
		return self.get_district_display()

class DistrictCollection(models.Model):
	district = models.CharField(
		max_length = 15,
		choices = districts,
	)
	collection = models.TextField(verbose_name = 'Details of collected items')

	class Meta:
		verbose_name = 'District: collection'
		verbose_name_plural = 'Districts: collections'



class RescueCamp(models.Model):
	name = models.CharField(max_length = 50, verbose_name = 'Camp-Name')
	location = models.TextField(verbose_name = 'Address', blank= True, null = True)
	district = models.CharField(max_length = 15, verbose_name = 'districts', choices = districts)
	taluk = models.CharField(max_length =50, verbose_name = 'Taluk')
	village = models.CharField(max_length = 50, verbose_name = 'village')
	contacts = models.TextField(verbose_name = 'Phone number', blank = True, null = True)
	facilities_available = models.TextField(blank = True, null = True, verbose_name = 'Facilities facilities_available( light, kitchen, toilets, etc.')
	data_entry_user = models.ForeignKey(
		User, 
		on_delete = models.SET_NULL, 
		blank = True, 
		null = True, 
		help_text = 'This camp coordinator page will be visiable only t this user')
	map_link = models.CharField(max_length = 250, verbose_name = 'Map link', blank = True, null = True, help_text = 'Copy and paste the full google maps link')
	latlng = models.CharField(max_length = 100, verbose_name = 'GPS Coordinates', blank = True, help_text = 'Comma separated latlng field. leave blank if you donot know it')
	total_people = models.IntegerField(null = True, blank = True, verbose_name = 'Total number of people')
	total_males = models.IntegerField(null = True, blank = True, verbose_name = 'Number of Males')
	total_females = models.IntegerField(null = True, blank = True, verbose_name = 'Number of females')
	total_infants = models.IntegerField(null = True, blank = True, verbose_name = 'Number of infants(<2y)')

	food_req = models.TextField(blank = True, null = True, verbose_name = 'Food')
	clothing_req = models.TextField(blank = True, null = True, verbose_name = 'Cloth')
	sanity_req = models.TextField(blank = True, null = True, verbose_name = 'Sanity')
	medical_req = models.TextField(blank = True, null = True, verbose_name = 'Medicine')
	other_req = models.CharField(max_length = 10, default = 'active', choices = relief_camp_status)

	class Meta:
		verbose_name = 'Relief: Camp'
		verbose_name_plural = 'Relief: Camps'

	def __str__(self):
		return self.name


class Person(models.Model):
	name = models.CharField(max_length = 30, blank = False, null = False, verbose_name = 'Name')
	phone = models.CharField(max_length = 11, null = True, blank = True, verbose_name = 'Mobile ')
	age = models.IntegerField(null = True, blank = True, verbose_name = 'Age')
	gender = models.IntegerField(choices = gender, verbose_name = 'Gender', null = True, blank = True)
	address = models.TextField(max_length = 150, null = True, blank = True, verbose_name = 'Address')
	district = models.CharField(max_length = 15, choices = districts, verbose_name = 'Residence District', null = True, blank = True)
	notes = models.TextField(max_length = 500, null = True, blank = True, verbose_name = 'Notes -')
	camp_at = models.ForeignKey(RescueCamp, on_delete = models.CASCADE, blank = False, null = False, verbose_name = 'Camp_Name')
	added_at = models.DateTimeField(auto_now_add = True)

	@property
	def sex(self):
		return {
		0:'Male',
		1: 'Female',
		2: 'Others'
		}.get(self.gender, 'Unknown')

	@property
	def district_name(self):
		return {
		'bar', 'Barguna',
		'bri', 'Barisal',
		'bhl', 'Bhola',
		'jhl', 'Jhalokati',
		'pat', 'Patuakhali',
		'pir', 'Pirojpur',
		'ban', 'Bandarban',
		'bhm', 'Brahmanbaria',
		'chd', 'Chandpur',
		'cht', 'Chittagong',
		'com', 'Comilla',
		'cox', 'Cox\'s Bazar',
		'fen', 'Feni',
		'khg', 'Khagrachhari',
		'lkh', 'Lakshmipur',
		'nkh', 'Noakhali',
		'rgm', 'Rangamati',
		'dhk', 'Dhaka',
		'frd', 'Faridpur',
		'gaz', 'Gazipur',
		'gop', 'Gopalganj',
		'kis', 'Kishoreganj',
		'mad', 'Madaripur',
		'man', 'Manikganj',
		'mun', 'Munshiganj',
		'nar', 'Narayanganj',
		'nas', 'Narsingdi',
		'raj', 'Rajbari',
		'sha', 'Shariatpur',
		'tan', 'Tangail',
		'bag', 'Bagerhat',
		'chu', 'Chuadanga',
		'jes', 'Jessore',
		'jhe', 'Jhenaidah',
		'khu', 'Khulna',
		'kus', 'Kushtai',
		'mag', 'Magura',
		'meh', 'Meherpur',
		'nri', 'Narail',
		'sat', 'Satkhira',
		'jam', 'Jamalpur',
		'mym', 'Mymensingh',
		}.get(self.district, 'Unknown')

	class Meta:
		verbose_name = 'Refegue: Refegue'
		verbose_name_plural = 'Refegue: Refegue'

	def __str__(self):
		return self.name

	


# Generated by Django 2.1 on 2018-08-20 09:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(choices=[('dha', 'Dhaka'), ('Cht', 'Chittagong'), ('raj', 'Rajshai'), ('bri', 'Barishal'), ('khu', 'Khulna'), ('syh', 'Sylhet'), ('ran', 'Rangpur'), ('mym', 'Mymensingh')], max_length=10, verbose_name='divisions')),
                ('district', models.CharField(choices=[('bar', 'Barguna'), ('bri', 'Barisal'), ('bhl', 'Bhola'), ('jhl', 'Jhalokati'), ('pat', 'Patuakhali'), ('pir', 'Pirojpur'), ('ban', 'Bandarban'), ('bhm', 'Brahmanbaria'), ('chd', 'Chandpur'), ('cht', 'Chittagong'), ('com', 'Comilla'), ('cox', "Cox's Bazar"), ('fen', 'Feni'), ('khg', 'Khagrachhari'), ('lkh', 'Lakshmipur'), ('nkh', 'Noakhali'), ('rgm', 'Rangamati'), ('dhk', 'Dhaka'), ('frd', 'Faridpur'), ('gaz', 'Gazipur'), ('gop', 'Gopalganj'), ('kis', 'Kishoreganj'), ('mad', 'Madaripur'), ('man', 'Manikganj'), ('mun', 'Munshiganj'), ('nar', 'Narayanganj'), ('nas', 'Narsingdi'), ('raj', 'Rajbari'), ('sha', 'Shariatpur'), ('tan', 'Tangail'), ('bag', 'Bagerhat'), ('chu', 'Chuadanga'), ('jes', 'Jessore'), ('jhe', 'Jhenaidah'), ('khu', 'Khulna'), ('kus', 'Kushtai'), ('mag', 'Magura'), ('meh', 'Meherpur'), ('nri', 'Narail'), ('sat', 'Satkhira'), ('jam', 'Jamalpur'), ('mym', 'Mymensingh')], max_length=15, verbose_name='districts')),
                ('organization', models.CharField(max_length=250, verbose_name='Name of organization')),
                ('organization_type', models.CharField(max_length=250, verbose_name='Type of Organization')),
                ('organiation_address', models.TextField(default='', verbose_name='Address of organization')),
                ('name', models.CharField(max_length=100, verbose_name='Contact person')),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format:"+999999999".upto 15 digits ', regex='^\\+?1?\\d{9, 15}$')])),
                ('description', models.TextField(verbose_name='About organization')),
                ('area', models.TextField(verbose_name='Area of volunteering')),
                ('location', models.CharField(max_length=500, verbose_name='Preferred location to volunteer')),
                ('is_spoc', models.BooleanField(default=False, verbose_name='Is point of Contact')),
                ('joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Volunteer: NGO',
                'verbose_name_plural': 'Volunteer: NGOs',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(choices=[('dha', 'Dhaka'), ('Cht', 'Chittagong'), ('raj', 'Rajshai'), ('bri', 'Barishal'), ('khu', 'Khulna'), ('syh', 'Sylhet'), ('ran', 'Rangpur'), ('mym', 'Mymensingh')], max_length=10, verbose_name='Division')),
                ('district', models.CharField(choices=[('bar', 'Barguna'), ('bri', 'Barisal'), ('bhl', 'Bhola'), ('jhl', 'Jhalokati'), ('pat', 'Patuakhali'), ('pir', 'Pirojpur'), ('ban', 'Bandarban'), ('bhm', 'Brahmanbaria'), ('chd', 'Chandpur'), ('cht', 'Chittagong'), ('com', 'Comilla'), ('cox', "Cox's Bazar"), ('fen', 'Feni'), ('khg', 'Khagrachhari'), ('lkh', 'Lakshmipur'), ('nkh', 'Noakhali'), ('rgm', 'Rangamati'), ('dhk', 'Dhaka'), ('frd', 'Faridpur'), ('gaz', 'Gazipur'), ('gop', 'Gopalganj'), ('kis', 'Kishoreganj'), ('mad', 'Madaripur'), ('man', 'Manikganj'), ('mun', 'Munshiganj'), ('nar', 'Narayanganj'), ('nas', 'Narsingdi'), ('raj', 'Rajbari'), ('sha', 'Shariatpur'), ('tan', 'Tangail'), ('bag', 'Bagerhat'), ('chu', 'Chuadanga'), ('jes', 'Jessore'), ('jhe', 'Jhenaidah'), ('khu', 'Khulna'), ('kus', 'Kushtai'), ('mag', 'Magura'), ('meh', 'Meherpur'), ('nri', 'Narail'), ('sat', 'Satkhira'), ('jam', 'Jamalpur'), ('mym', 'Mymensingh')], max_length=15, verbose_name='District')),
                ('location', models.CharField(max_length=500, verbose_name='Location')),
                ('requestee', models.CharField(max_length=100, verbose_name='Requestee')),
                ('requestee_phone', models.CharField(max_length=10, verbose_name='Requestee_phone')),
                ('latlng', models.CharField(blank=True, max_length=100, verbose_name='GPS-Coordinate - GPS')),
                ('latlng_accuracy', models.CharField(blank=True, max_length=100, verbose_name='GPS-Accuracy')),
                ('is_request_for_others', models.BooleanField(default=False, help_text='If it is enabled, no need to consider lat and lng', verbose_name='Requesting for others-')),
                ('needwater', models.BooleanField(verbose_name='Water')),
                ('needfooed', models.BooleanField(verbose_name='Food')),
                ('needcloth', models.BooleanField(verbose_name='Cloth')),
                ('needmed', models.BooleanField(verbose_name='Medicine')),
                ('needtoilet', models.BooleanField(verbose_name='Toilet')),
                ('needkit_util', models.BooleanField(verbose_name='Kitchen Utilities')),
                ('needrescue', models.BooleanField(verbose_name='Rescue')),
                ('detailwater', models.CharField(blank=True, max_length=250, verbose_name='Detail for required water')),
                ('detailfood', models.CharField(blank=True, max_length=250, verbose_name='Detail for requird food')),
                ('detailcloth', models.CharField(blank=True, max_length=250, verbose_name='Detail for requird cloth')),
                ('detailmed', models.CharField(blank=True, max_length=250, verbose_name='Detail for required medicine')),
                ('detailtoilet', models.CharField(blank=True, max_length=250, verbose_name='Detail for required toilet')),
                ('detailkt_utils', models.CharField(blank=True, max_length=250, verbose_name='Detail for required kitchen utilities')),
                ('detailrescue', models.CharField(blank=True, max_length=250, verbose_name='Detail for required rescue')),
                ('needothers', models.CharField(blank=True, max_length=500, verbose_name='required others')),
                ('status', models.CharField(choices=[('new', 'New'), ('pro', 'In progress'), ('sup', 'Supplied')], default='new', max_length=10)),
                ('supply_details', models.CharField(blank=True, max_length=10)),
                ('dateadd', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Rescue: Request',
                'verbose_name_plural': 'Rescue : Resquest',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(choices=[('dha', 'Dhaka'), ('Cht', 'Chittagong'), ('raj', 'Rajshai'), ('bri', 'Barishal'), ('khu', 'Khulna'), ('syh', 'Sylhet'), ('ran', 'Rangpur'), ('mym', 'Mymensingh')], max_length=10, verbose_name='Divisions')),
                ('district', models.CharField(choices=[('bar', 'Barguna'), ('bri', 'Barisal'), ('bhl', 'Bhola'), ('jhl', 'Jhalokati'), ('pat', 'Patuakhali'), ('pir', 'Pirojpur'), ('ban', 'Bandarban'), ('bhm', 'Brahmanbaria'), ('chd', 'Chandpur'), ('cht', 'Chittagong'), ('com', 'Comilla'), ('cox', "Cox's Bazar"), ('fen', 'Feni'), ('khg', 'Khagrachhari'), ('lkh', 'Lakshmipur'), ('nkh', 'Noakhali'), ('rgm', 'Rangamati'), ('dhk', 'Dhaka'), ('frd', 'Faridpur'), ('gaz', 'Gazipur'), ('gop', 'Gopalganj'), ('kis', 'Kishoreganj'), ('mad', 'Madaripur'), ('man', 'Manikganj'), ('mun', 'Munshiganj'), ('nar', 'Narayanganj'), ('nas', 'Narsingdi'), ('raj', 'Rajbari'), ('sha', 'Shariatpur'), ('tan', 'Tangail'), ('bag', 'Bagerhat'), ('chu', 'Chuadanga'), ('jes', 'Jessore'), ('jhe', 'Jhenaidah'), ('khu', 'Khulna'), ('kus', 'Kushtai'), ('mag', 'Magura'), ('meh', 'Meherpur'), ('nri', 'Narail'), ('sat', 'Satkhira'), ('jam', 'Jamalpur'), ('mym', 'Mymensingh')], max_length=15, verbose_name='districts')),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_mobile', message='Please enter 10 digit mobile number', regex='^[6-9]\\d{9}$')], verbose_name='Phone')),
                ('organization', models.CharField(max_length=250, verbose_name='Organization')),
                ('address', models.TextField(verbose_name='address')),
                ('area', models.CharField(choices=[('dcr', 'Doctor'), ('hsv', 'Health Service'), ('elw', 'Electrical Works'), ('mew', 'Mechanical Works'), ('cvw', 'Civil Works'), ('plw', 'Plumbing works'), ('vls', 'Vehical support'), ('ckg', 'Cooking'), ('rlo', 'relief operation'), ('cln', 'Cleaning'), ('bot', 'Boat Service'), ('rck', 'Rock Climbing'), ('oth', 'Others')], max_length=15, verbose_name='Area of volunteering')),
                ('is_spoc', models.BooleanField(default=False, verbose_name='Is point of Contact')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Volunteer: individual',
                'verbose_name_plural': 'Volunteer: individual',
            },
        ),
    ]

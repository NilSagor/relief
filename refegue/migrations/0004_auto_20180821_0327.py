# Generated by Django 2.1 on 2018-08-21 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('refegue', '0003_districtcollection_districtmanager_districtneed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Mobile ')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female'), (2, 'Others')], null=True, verbose_name='Gender')),
                ('address', models.TextField(blank=True, max_length=150, null=True, verbose_name='Address')),
                ('district', models.CharField(blank=True, choices=[('bar', 'Barguna'), ('bri', 'Barisal'), ('bhl', 'Bhola'), ('jhl', 'Jhalokati'), ('pat', 'Patuakhali'), ('pir', 'Pirojpur'), ('ban', 'Bandarban'), ('bhm', 'Brahmanbaria'), ('chd', 'Chandpur'), ('cht', 'Chittagong'), ('com', 'Comilla'), ('cox', "Cox's Bazar"), ('fen', 'Feni'), ('khg', 'Khagrachhari'), ('lkh', 'Lakshmipur'), ('nkh', 'Noakhali'), ('rgm', 'Rangamati'), ('dhk', 'Dhaka'), ('frd', 'Faridpur'), ('gaz', 'Gazipur'), ('gop', 'Gopalganj'), ('kis', 'Kishoreganj'), ('mad', 'Madaripur'), ('man', 'Manikganj'), ('mun', 'Munshiganj'), ('nar', 'Narayanganj'), ('nas', 'Narsingdi'), ('raj', 'Rajbari'), ('sha', 'Shariatpur'), ('tan', 'Tangail'), ('bag', 'Bagerhat'), ('chu', 'Chuadanga'), ('jes', 'Jessore'), ('jhe', 'Jhenaidah'), ('khu', 'Khulna'), ('kus', 'Kushtai'), ('mag', 'Magura'), ('meh', 'Meherpur'), ('nri', 'Narail'), ('sat', 'Satkhira'), ('jam', 'Jamalpur'), ('mym', 'Mymensingh')], max_length=15, null=True, verbose_name='Residence District')),
                ('notes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Notes -')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Refegue: Refegue',
                'verbose_name_plural': 'Refegue: Refegue',
            },
        ),
        migrations.CreateModel(
            name='RescueCamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Camp-Name')),
                ('location', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('district', models.CharField(choices=[('bar', 'Barguna'), ('bri', 'Barisal'), ('bhl', 'Bhola'), ('jhl', 'Jhalokati'), ('pat', 'Patuakhali'), ('pir', 'Pirojpur'), ('ban', 'Bandarban'), ('bhm', 'Brahmanbaria'), ('chd', 'Chandpur'), ('cht', 'Chittagong'), ('com', 'Comilla'), ('cox', "Cox's Bazar"), ('fen', 'Feni'), ('khg', 'Khagrachhari'), ('lkh', 'Lakshmipur'), ('nkh', 'Noakhali'), ('rgm', 'Rangamati'), ('dhk', 'Dhaka'), ('frd', 'Faridpur'), ('gaz', 'Gazipur'), ('gop', 'Gopalganj'), ('kis', 'Kishoreganj'), ('mad', 'Madaripur'), ('man', 'Manikganj'), ('mun', 'Munshiganj'), ('nar', 'Narayanganj'), ('nas', 'Narsingdi'), ('raj', 'Rajbari'), ('sha', 'Shariatpur'), ('tan', 'Tangail'), ('bag', 'Bagerhat'), ('chu', 'Chuadanga'), ('jes', 'Jessore'), ('jhe', 'Jhenaidah'), ('khu', 'Khulna'), ('kus', 'Kushtai'), ('mag', 'Magura'), ('meh', 'Meherpur'), ('nri', 'Narail'), ('sat', 'Satkhira'), ('jam', 'Jamalpur'), ('mym', 'Mymensingh')], max_length=15, verbose_name='districts')),
                ('taluk', models.CharField(max_length=50, verbose_name='Taluk')),
                ('village', models.CharField(max_length=50, verbose_name='village')),
                ('contacts', models.TextField(blank=True, null=True, verbose_name='Phone number')),
                ('facilities_available', models.TextField(blank=True, null=True, verbose_name='Facilities facilities_available( light, kitchen, toilets, etc.')),
                ('map_link', models.CharField(blank=True, help_text='Copy and paste the full google maps link', max_length=250, null=True, verbose_name='Map link')),
                ('latlng', models.CharField(blank=True, help_text='Comma separated latlng field. leave blank if you donot know it', max_length=100, verbose_name='GPS Coordinates')),
                ('total_people', models.IntegerField(blank=True, null=True, verbose_name='Total number of people')),
                ('total_males', models.IntegerField(blank=True, null=True, verbose_name='Number of Males')),
                ('total_females', models.IntegerField(blank=True, null=True, verbose_name='Number of females')),
                ('total_infants', models.IntegerField(blank=True, null=True, verbose_name='Number of infants(<2y)')),
                ('food_req', models.TextField(blank=True, null=True, verbose_name='Food')),
                ('clothing_req', models.TextField(blank=True, null=True, verbose_name='Cloth')),
                ('sanity_req', models.TextField(blank=True, null=True, verbose_name='Sanity')),
                ('medical_req', models.TextField(blank=True, null=True, verbose_name='Medicine')),
                ('other_req', models.CharField(choices=[('active', 'Activate'), ('closed', 'Closed')], default='active', max_length=10)),
                ('data_entry_user', models.ForeignKey(blank=True, help_text='This camp coordinator page will be visiable only t this user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Relief: Camp',
                'verbose_name_plural': 'Relief: Camps',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='camp_at',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refegue.RescueCamp', verbose_name='Camp_Name'),
        ),
    ]

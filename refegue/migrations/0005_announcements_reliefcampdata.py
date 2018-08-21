# Generated by Django 2.1 on 2018-08-21 10:53

from django.db import migrations, models
import refegue.models


class Migration(migrations.Migration):

    dependencies = [
        ('refegue', '0004_auto_20180821_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateadded', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='L', max_length=20, verbose_name='Priority')),
                ('image', models.ImageField(blank=True, upload_to=refegue.models.upload_to)),
                ('upload', models.FileField(blank=True, upload_to=refegue.models.upload_to)),
                ('is_pinned', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Announcement: News',
                'verbose_name_plural': 'Announcements: News',
            },
        ),
        migrations.CreateModel(
            name='ReliefCampData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, verbose_name='Details of requirements')),
                ('district', models.CharField(blank=True, choices=[('bar', 'Barguna'), ('bri', 'Barisal'), ('bhl', 'Bhola'), ('jhl', 'Jhalokati'), ('pat', 'Patuakhali'), ('pir', 'Pirojpur'), ('ban', 'Bandarban'), ('bhm', 'Brahmanbaria'), ('chd', 'Chandpur'), ('cht', 'Chittagong'), ('com', 'Comilla'), ('cox', "Cox's Bazar"), ('fen', 'Feni'), ('khg', 'Khagrachhari'), ('lkh', 'Lakshmipur'), ('nkh', 'Noakhali'), ('rgm', 'Rangamati'), ('dhk', 'Dhaka'), ('frd', 'Faridpur'), ('gaz', 'Gazipur'), ('gop', 'Gopalganj'), ('kis', 'Kishoreganj'), ('mad', 'Madaripur'), ('man', 'Manikganj'), ('mun', 'Munshiganj'), ('nar', 'Narayanganj'), ('nas', 'Narsingdi'), ('raj', 'Rajbari'), ('sha', 'Shariatpur'), ('tan', 'Tangail'), ('bag', 'Bagerhat'), ('chu', 'Chuadanga'), ('jes', 'Jessore'), ('jhe', 'Jhenaidah'), ('khu', 'Khulna'), ('kus', 'Kushtai'), ('mag', 'Magura'), ('meh', 'Meherpur'), ('nri', 'Narail'), ('sat', 'Satkhira'), ('jam', 'Jamalpur'), ('mym', 'Mymensingh')], max_length=15, null=True, verbose_name='Districts')),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Phone')),
            ],
            options={
                'verbose_name': 'Relief: Camp Data',
                'verbose_name_plural': 'Relief: Camp Datas',
            },
        ),
    ]

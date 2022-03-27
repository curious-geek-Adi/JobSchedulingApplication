# Generated by Django 2.2.19 on 2021-07-11 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('cid', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Company_ID:')),
                ('name', models.CharField(max_length=20, verbose_name='Company Name:')),
                ('city', models.CharField(max_length=15, verbose_name='City:')),
                ('zipcode', models.CharField(max_length=15, verbose_name='Zipcode:')),
            ],
        ),
        migrations.CreateModel(
            name='contractor',
            fields=[
                ('ccid', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Contractor_ID:')),
                ('name', models.CharField(max_length=20, verbose_name='Contractor Name')),
                ('city', models.CharField(max_length=15, verbose_name='City:')),
                ('zipcode', models.CharField(max_length=15, verbose_name='Zipcode')),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('job_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=20)),
                ('contractor', models.CharField(max_length=20)),
                ('Date_job', models.DateField()),
                ('time_job', models.TimeField()),
            ],
        ),
    ]

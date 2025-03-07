# Generated by Django 5.0.6 on 2024-07-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('course', models.CharField(max_length=20)),
                ('classroom', models.CharField(max_length=20)),
                ('date_of_the_week', models.DateField()),
            ],
        ),
    ]

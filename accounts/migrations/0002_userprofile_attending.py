# Generated by Django 3.2.6 on 2021-08-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='attending',
            field=models.ManyToManyField(blank=True, related_name='attending', to='events.Event'),
        ),
    ]
# Generated by Django 2.2.5 on 2019-09-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0022_auto_20190928_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='userarticle',
            name='Article_writer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

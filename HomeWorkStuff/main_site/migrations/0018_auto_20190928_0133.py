# Generated by Django 2.2.5 on 2019-09-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0017_userarticle_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userarticle',
            name='USER',
            field=models.CharField(max_length=255),
        ),
    ]

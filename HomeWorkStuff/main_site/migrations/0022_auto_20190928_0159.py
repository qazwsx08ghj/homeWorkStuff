# Generated by Django 2.2.5 on 2019-09-27 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0021_auto_20190928_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userarticle',
            name='USER',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

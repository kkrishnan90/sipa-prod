# Generated by Django 4.1.1 on 2022-09-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_nonmembermodel_ordermodel_family_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]

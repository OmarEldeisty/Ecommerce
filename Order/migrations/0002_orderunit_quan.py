# Generated by Django 4.0.1 on 2022-01-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderunit',
            name='quan',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
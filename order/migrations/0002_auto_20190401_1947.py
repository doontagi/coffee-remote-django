# Generated by Django 2.1.7 on 2019-04-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordernumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='pickuptime',
            field=models.IntegerField(),
        ),
    ]

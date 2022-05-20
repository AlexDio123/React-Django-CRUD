# Generated by Django 4.0.1 on 2022-01-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
                ('categoryLevel', models.IntegerField()),
                ('categoryParentID', models.IntegerField()),
                ('BestOfferEnabled', models.BooleanField(default=True)),
                ('AutoPayEnabled', models.BooleanField(default=True)),
            ],
        ),
    ]

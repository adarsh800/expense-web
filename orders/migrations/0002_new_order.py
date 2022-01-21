# Generated by Django 4.0.1 on 2022-01-17 16:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_new_order', models.CharField(max_length=255)),
                ('second_name_new_order', models.CharField(max_length=255)),
                ('email_new_order', models.CharField(max_length=255)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address_new_order', models.CharField(blank=True, max_length=255, null=True)),
                ('address2_new_order', models.CharField(blank=True, max_length=255, null=True)),
                ('city_new_order', models.CharField(max_length=255)),
                ('pincode_new_order', models.PositiveIntegerField(default=0, max_length=6)),
                ('state_new_order', models.CharField(max_length=255)),
            ],
        ),
    ]
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now
# Create your models here.


class UserPreference(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)+'s' + 'preferences'

class new_order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, blank=False, null=True)
    date_new_order = models.DateTimeField(default=now)
    order_details = models.CharField(max_length=266, blank=True, null=True)
    first_name_new_order = models.CharField(max_length=255, blank=False, null=False)
    second_name_new_order = models.CharField(max_length=255, blank=False, null=False)
    email_new_order = models.CharField(max_length=255, blank=False, null=False)
    phone_number_new_order = PhoneNumberField()
    address_new_order = models.CharField(max_length=255, blank=True, null=True)
    address2_new_order = models.CharField(max_length=255, blank=True, null=True)
    city_new_order = models.CharField(max_length=255, blank=False, null=False)
    pincode_new_order = models.PositiveIntegerField(default=0, blank=False)
    state_new_order = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.date_new_order
    
    # SORT ORDER BY
    class Meta:
        ordering:['-date_new_order']
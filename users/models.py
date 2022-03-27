

from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_SELECTION = [
    ('NS', 'Not Specified'),
    ('M', 'Male'),
    ('F', 'Female'),
]


USER_TYPES = [
    ('customer', 'Customer'),
    ('enterprise', 'Enterprise'),
    ('contractor', 'Contractor'),
]


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=20,
                              choices=GENDER_SELECTION,
                              default='NS')
    user_type = models.CharField(max_length=20,
                                 choices=USER_TYPES,
                                 default='Customer')
    phone_number = models.CharField(max_length=30)
    profile_image = models.ImageField(
        upload_to='users/profileImages',
        blank=True,
        default="users/default/default_user.jpg")


from django.db import models
from django.contrib.auth.models import User

ADMIN = 1
VIPClient = 2
CLIENT = 3
USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIPClient, "VIP-Client"),
    (CLIENT, "CLIENT")
)
MALE = 1
FEMALE = 2
GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
)

class CustomUser(User):
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name="тип пользователя", default=CLIENT)
    phone_number = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE)
from django.db import models
from django.contrib.auth.models import AbstractUser #상속

class User(AbstractUser):
    pass


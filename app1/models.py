from django.db import models

# Create your models here.
class Register_users(models.Model):
    login = models.CharField(max_length=20, blank=False)
    password_hash = models.CharField(max_length=50, blank=False)

    def __str__(self) -> str:
        return self.login
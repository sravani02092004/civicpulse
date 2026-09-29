from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('CITIZEN', 'Citizen'),
        ('NGO', 'NGO Representative'),
        ('ADMIN', 'Municipal Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CITIZEN')
    phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class NGOProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ngo_profile')
    organization_name = models.CharField(max_length=150)
    category_focus = models.CharField(max_length=100, help_text="e.g., Garbage, Road Damage, Water Safety")
    operating_location = models.CharField(max_length=100)

    def __str__(self):
        return self.organization_name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrates = models.FloatField()

    def __str__(self):
        return self.name

class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
    consumed_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    calories_goal = models.FloatField(default=2000)

    def __str__(self):
        return f"{self.user.username} Profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

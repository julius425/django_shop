from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumber
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.timezone import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    user_pic = models.ImageField(blank=True)
    email = models.EmailField(blank=True)
    phone_number = PhoneNumber()
    address = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}\'s profile.'.format(self.user.username)

    def get_absolute_url(self):
        return reverse('accounts:profile', args=[self.pk])

    def get_completed_orders(self):
        completed = self.orders.filter(ordered=True)
        return completed

    def get_pending_orders(self):
        pending = self.orders.filter(ordered=False)
        return pending

    def edit_profile(self):
        return reverse('accounts:edit', args=[self.pk])


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


post_save.connect(create_profile, sender=User)


from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Concert(models.Model):
    # concert_name
    concert_name = models.CharField(max_length=255, null=True)

    # duration
    duration = models.IntegerField(null=True)

    # city
    city = models.CharField(max_length=255, null=True)

    # date
    date = models.DateTimeField(null=True, default=datetime.now())

    def __str__(self):
        return self.concert_name


class ConcertAttending(models.Model):
    class AttendingChoices(models.TextChoices):
        NOTHING = "-", _("-")
        NOT_ATTENDING = "Not Attending", _("Not Attending")
        ATTENDING = "Attending", _("Attending")

    concert = models.ForeignKey(
        Concert, null=True, on_delete=models.CASCADE, related_name="attendee"
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    attending = models.CharField(
        max_length=100,
        choices=AttendingChoices.choices,
        default=AttendingChoices.NOTHING,
    )

    class Meta:
        unique_together = ['concert', 'user']

    def __str__(self):
        return self.attending


class Photo(models.Model):
    # id
    id = models.AutoField(primary_key=True)

    # pic_url
    pic_url = models.CharField(max_length=1000, null=True)

    # event_country
    event_country = models.CharField(max_length=255, null=True)

    # event_state
    event_state = models.CharField(max_length=255, null=True)

    # event_city
    event_city = models.CharField(max_length=255, null=True)

    # event_date
    event_date = models.DateTimeField(null=True, default=datetime.now())

    class Meta:
        managed = False

    def __str__(self):
        return self.pic_url


class Song(models.Model):
    # id
    id = models.AutoField(primary_key=True)

    # title
    title = models.CharField(max_length=255, null=True)

    # lyrics
    lyrics = models.TextField(null=True)

    class Meta:
        managed = False

    def __str__(self):
        return self.title

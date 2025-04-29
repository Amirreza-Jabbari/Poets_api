from django.db import models

class GolestanHikayat(models.Model):
    bab     = models.CharField(max_length=50)
    hekayat = models.IntegerField()
    content    = models.TextField()

    class Meta:
        db_table = 'golestan_hikayat'


class Hafez(models.Model):
    urn     = models.CharField(max_length=255, primary_key=True)
    section = models.TextField()
    text    = models.TextField()

    class Meta:
        db_table = 'hafez'
        managed = False        # don’t try to create/alter the table


class Khayyam(models.Model):
    urn     = models.CharField(max_length=255, primary_key=True)
    section = models.TextField()
    text    = models.TextField()

    class Meta:
        db_table = 'khayyam'
        managed = False


class Moulavi(models.Model):
    urn     = models.CharField(max_length=255, primary_key=True)
    section = models.TextField()
    text    = models.TextField()

    class Meta:
        db_table = 'moulavi'
        managed = False
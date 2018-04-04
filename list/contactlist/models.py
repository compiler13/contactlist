# -*- coding: utf-8 -*-


from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30, default=None, null=True)
    phone = models.CharField(max_length=12, default=None, null=True)
    email = models.CharField(max_length=30, default=None, null=True)
    profession = models.CharField(max_length=20, default=None, null=True)


def __str__(self):
    return '{} : {} : {} : {}'.format(
        self.name,
        self.phone,
        self.email,
        self.profession,
    )

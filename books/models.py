# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Author(models.Model):
    author_firstname = models.CharField(max_length=100)
    author_lastname = models.CharField(max_length=100)

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Stores(models.Model):
    store_name = models.CharField(max_length =100)


class Sales(models.Model):
    Store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    Book = models.ForeignKey(Books, on_delete = models.CASCADE)
    sold = models.IntegerField()


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Superhero(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    superpower = models.CharField(max_length=100)
    is_good = models.BooleanField()
    is_male = models.BooleanField()
    rating = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=200)
    is_male = models.BooleanField()
    
    def __str__(self):
        return self.name 
        

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return self.make + " " + self.model + " " + str(self.year)

class Stock(models.Model):
    company = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    market_cap = models.FloatField()
    
    def __str__(self):
        return self.company

class Message(models.Model):
    text = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text


class Employee(models.Model):
    employee = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    salary = models.FloatField()
    
    def __str__(self):
        return self.employee


class Credit_Card(models.Model):
    number = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
        
class Friend(models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Graffiti(models.Model):
    
    message = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    
    def __str__(self):
        return self.message

class Food(models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name

class Task(models.Model):
    item = models.CharField(max_length=200)
    priority = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item

class Ajax_Task(models.Model):
    item = models.CharField(max_length=200)
    priority = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item

class Superhero2(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    superpower = models.CharField(max_length=100)
    is_good = models.BooleanField()
    is_male = models.BooleanField()
    rating = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Animal2(models.Model):
    name = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=200)
    is_male = models.BooleanField()
    
    def __str__(self):
        return self.name 
        

class Car2(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return self.make + " " + self.model + " " + str(self.year)

class Stock2(models.Model):
    company = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    market_cap = models.FloatField()
    
    def __str__(self):
        return self.company

class Message2(models.Model):
    text = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text


class Employee2(models.Model):
    employee = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    salary = models.FloatField()
    
    def __str__(self):
        return self.employee


class Credit_Card2(models.Model):
    number = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Blog2(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
        
class Friend2(models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Graffiti2(models.Model):
    
    message = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    
    def __str__(self):
        return self.message

class Food2(models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Contact2(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Athlete2(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name

class Task2(models.Model):
    item = models.CharField(max_length=200)
    priority = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item

class Ajax_Task2(models.Model):
    item = models.CharField(max_length=200)
    priority = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item


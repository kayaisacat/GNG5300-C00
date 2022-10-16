# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.db import models
from django.db import models
# Create your models here
# from django.db.models import Model
# Created an empty model
# class GeeksModel(Model):
# 	pass

# import the standard Django Model
# from built-in library 

# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
		# fields of the model
	title = models.CharField(max_length = 200)
	description = models.TextField()
	# last_modified = models.DateTimeField(auto_now_add = True)
	# img = models.ImageField(upload_to = "images/")

		# renames the instances of the model
		# with their title name
	def __str__(self):
		return self.title


from django.db import models

class Logbook(models.Model):
	id 					= models.AutoField(primary_key = True)
	user				= models.IntegerField( unique=True)
	created_date        = models.DateField(auto_now_add=True)
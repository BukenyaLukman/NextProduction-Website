from django.db import models
from PIL import Image



class BackgroundIntro(models.Model):
	header	= models.CharField(max_length=300)
	description = models.CharField(max_length=750)
	background_image = models.ImageField(upload_to='images')

	def __str__(self):
		return self.header


class NextService(models.Model):
	service_name = models.CharField(max_length=100,blank=True, null=True)
	image =  models.ImageField(upload_to='images')
	description = models.CharField(max_length=255, null=True)


	def __str__(self):
		return self.service_name


class FilmProduction(models.Model):
	image = models.ImageField(upload_to='images')
	service_name = models.CharField(max_length=100, null=True)


	def __str__(self):
		return self.service_name

class Projects(models.Model):
	clients = models.IntegerField(default=1)
	projects = models.IntegerField(default=1)
	hours_of_support = models.IntegerField(default=1)
	hard_work = models.IntegerField(default=1)
	
	def __str__(self):
		return str(self.clients) + "--" + str(self.projects)

class RadioAdverts(models.Model):
	image = models.ImageField(upload_to='images')
	title = models.CharField(max_length=100, null=True)
	description = models.CharField(max_length=100, null=True)


	def __str__(self):
		return self.title

class OurClients(models.Model):
	image = models.ImageField(upload_to='images')
	name = models.CharField(max_length=100, null=True)


	def __str__(self):
		return self.name

class Testimonials(models.Model):
	client_image = models.ImageField(upload_to='images')
	client_name = models.CharField(max_length=200, null=True)
	client_profession = models.CharField(max_length=100, null=True)
	comment = models.TextField(null=True,blank=True)

	def __str__(self):
		return self.client_name + "-" + self.client_profession

class Team(models.Model):
	image = models.ImageField(upload_to='images')
	name = models.CharField(max_length=200, null=True)
	position = models.CharField(max_length=200, null=True)
	twitter = models.CharField(max_length=300, blank=True, null=True)
	facebook = models.CharField(max_length=300, blank=True, null=True)
	gmail = models.CharField(max_length=300, blank=True, null=True)
	linked = models.CharField(max_length=300, blank=True, null=True)

	def __str__(self):
		return self.name + "-" + self.position

class Contact(models.Model):
	sender = models.CharField(max_length=200, null=True)
	subject = models.CharField(max_length=200, null=True)
	message = models.TextField(max_length=500, null=True)
	email = models.EmailField(max_length=255, null=True)

	def __str__(self):
		return self.sender + "-" + self.subject
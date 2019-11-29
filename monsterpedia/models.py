from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Species(models.Model):
	"""docstring for ClassName"""
	namespecies = models.CharField(max_length=200)

	def __str__(self):
		return self.namespecies

class Armor(models.Model):
	"""docstring for ClassName"""
	namearmor = models.CharField(max_length=200)
	monster = models.ForeignKey('Monster', on_delete=models.SET_NULL, null=True)

	information = models.CharField(max_length=3000)
	imagearmor = models.ImageField(upload_to='photos')

	class Meta:
		ordering = ['namearmor', 'monster']

	def __str__(self):
		return f'{self.namearmor}, {self.monster}'

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('armor-detail', args=[str(self.id)])


class Monster(models.Model):
	"""docstring for ClassName"""
	namemonster = models.CharField(max_length=200)
	title = models.CharField(max_length=500)
	species = models.ForeignKey('Species', on_delete=models.SET_NULL, null=True)
	elements = models.CharField(max_length=500)
	state = models.CharField(max_length=500)
	weak = models.CharField(max_length=100)
	habitat = models.CharField(max_length=1000)
	size = models.CharField(max_length=10)
	relative = models.CharField(max_length=500)
	imagemonster = models.ImageField(blank=True, null=True,
		upload_to='photos/%Y/%m/%D/')

	class Meta:
		ordering = ['namemonster', 'title']

	def __str__(self):
		return f'{self.namemonster}, {self.title}'

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('monster-detail', args=[str(self.id)])
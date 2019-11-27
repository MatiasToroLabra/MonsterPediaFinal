from django.test import TestCase
from monsterpedia.models import Species


# Create your tests here.
class SpeciesModelTest(TestCase):
	@classmethod 
	def setUpTestData(cls):
		Species.objects.create(namespecies='Elder Dragon')

	def test_first_name_label(self):
		species=Species.objects.get(id=1)
		field_label = Species._meta.get_field('namespecies').verbose_name
		self.assertEqual(field_label, 'namespecies')

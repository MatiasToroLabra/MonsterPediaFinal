from django.test import TestCase
from monsterpedia.models import Armor


# Create your tests here.
class SpeciesModelTest(TestCase):
	@classmethod 
	def setUpTestData(cls):
		Armor.objects.create(namearmor='Valstrax Armor',  information='Descripcion')

	def test_first_name_label(self):
		armor=Armor.objects.get(id=1)
		field_label = Armor._meta.get_field('namearmor').verbose_name
		self.assertEqual(field_label, 'namearmor')

	def test_information_label(self):
		armor=Armor.objects.get(id=1)
		field_label = Armor._meta.get_field('information').verbose_name
		self.assertEqual(field_label, 'information')

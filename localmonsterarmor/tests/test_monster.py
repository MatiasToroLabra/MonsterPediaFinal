from django.test import TestCase
from monsterpedia.models import Monster


# Create your tests here.
class MonsterModelTest(TestCase):
	@classmethod 
	def setUpTestData(cls):
		Monster.objects.create(namemonster='valstrax', title='Dragon Cometa', elements='Draco', state='Plaga de Draco', weak='Hielo', habitat='Monte Cielo', size='20000', relative='NA')

	def test_first_name_label(self):
		monster=Monster.objects.get(id=1)
		field_label = Monster._meta.get_field('namemonster').verbose_name
		self.assertEqual(field_label, 'namemonster')

	def test_title_label(self):
		monster=Monster.objects.get(id=1)
		field_label = Monster._meta.get_field('title').verbose_name
		self.assertEqual(field_label, 'title')

	def test_elements_label(self):
		monster=Monster.objects.get(id=1)
		field_label = Monster._meta.get_field('elements').verbose_name
		self.assertEqual(field_label, 'elements')

	def test_state_label(self):
		monster=Monster.objects.get(id=1)
		field_label = Monster._meta.get_field('state').verbose_name
		self.assertEqual(field_label, 'state')

	def test_weak_label(self):
		monster=Monster.objects.get(id=1)
		field_label = Monster._meta.get_field('weak').verbose_name
		self.assertEqual(field_label, 'weak')

	def test_habitat_label(self):
		monster=Monster.objects.get(id=1)
		field_label = Monster._meta.get_field('habitat').verbose_name
		self.assertEqual(field_label, 'habitat')

	def test_size_label(self):
		monster=Monster.objects.get(id=1)
		field_label = Monster._meta.get_field('size').verbose_name
		self.assertEqual(field_label, 'size')

	def test_relative_label(self):
		monster=Monster.objects.get(id=1)
		field_label = Monster._meta.get_field('relative').verbose_name
		self.assertEqual(field_label, 'relative')
		


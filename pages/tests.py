from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_by_name(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        response = self.client.get(reverse('pages:home'))
        self.assertTemplateUsed('home.html')

    def test_correct_content(self):
        response = self.client.get(reverse('pages:home'))
        self.assertContains(response, '<h1>HomePage</h1>')


class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_by_name(self):
        response = self.client.get(reverse('pages:about'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        response = self.client.get(reverse('pages:about'))
        self.assertTemplateUsed('about.html')

    def test_correct_content(self):
        response = self.client.get(reverse('pages:about'))
        self.assertContains(response, '<h1>About page</h1>')

from django.test import TestCase, Client
from django.urls import reverse

from refegue.models import Request, Volunteer, Contributor, NGO, DistrictNeed, RescueCamp




class TemplateViewTests(TestCase):
	def check_template_view_response(self, url, template_name):
		client = Client()
		response = client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, template_name)
		return response


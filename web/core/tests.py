from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TestFindEndpoint(APITestCase):

    def test_find_endpoint_wrong_method(self):
        """Test for the Find endpoint calling with POST."""
        url = reverse('nfe_find', kwargs={"access_key": "35140330290824000104550010003715421390782397"})
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_find_endpoint_valid_key(self):
        """Test for the Find endpoint passing a valid Access_key."""
        url = reverse('nfe_sync')
        response = self.client.get(url, format='json')
        url = reverse('nfe_find', kwargs={"access_key": "35140330290824000104550010003715421390782397"})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_find_endpoint_missing_key(self):
        """Test for the Find endpoint passing a valid Access_key."""
        url = reverse('nfe_sync')
        response = self.client.get(url, format='json')
        url = reverse('nfe_find', kwargs={"access_key": "35140330290824000104550010003715421390782394"})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
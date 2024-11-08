from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class DifferenceAPITestCase(APITestCase):
    fixtures = ['differences.json']

    def test_that_10_works(self):
        url = reverse('difference')
        response = self.client.get(url, {'number': 10})
        assert response.status_code == 200
        assert response.data['number'] == 10
        assert response.data['value'] == 2640
        assert response.data['occurrences'] == 0

    def test_a_few_invalid_calls(self):
        url = reverse('difference')

        # Not passing in a number query param
        response = self.client.get(url, {})
        assert response.status_code == 400

        # Passing in too large a number query param
        response = self.client.get(url, {'number': 101})
        assert response.status_code == 400

        # Passing in a string instead of an int for the number query param
        response = self.client.get(url, {'number': 'ten'})
        assert response.status_code == 400


class TripletAPITestCase(APITestCase):

    def test_that_345_works_and_is_triplet(self):
        url = reverse('triplet')
        response = self.client.get(url, {'a': 3, 'b': 4, 'c': 5})
        assert response.status_code == 200
        assert response.data['a'] == 3
        assert response.data['b'] == 4
        assert response.data['c'] == 5
        assert response.data['is_triplet'] == True  # noqa: E712
        assert response.data['product'] == 60
        assert response.data['occurrences'] == 0

    def test_that_346_does_works_and_is_not_triplet(self):
        url = reverse('triplet')
        response = self.client.get(url, {'a': 3, 'b': 4, 'c': 6})
        assert response.status_code == 200
        assert response.data['a'] == 3
        assert response.data['b'] == 4
        assert response.data['c'] == 6
        assert response.data['is_triplet'] == False  # noqa: E712
        assert response.data['product'] == 72
        assert response.data['occurrences'] == 0

    def test_that_occurrences_gets_incremented(self):
        url = reverse('triplet')

        response = self.client.get(url, {'a': 1, 'b': 2, 'c': 3})
        assert response.status_code == 200
        assert response.data['occurrences'] == 0

        response = self.client.get(url, {'a': 1, 'b': 2, 'c': 3})
        assert response.status_code == 200
        assert response.data['occurrences'] == 1


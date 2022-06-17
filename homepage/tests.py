from django.http import FileResponse, HttpResponse
from django.test import TestCase

from django.test.client import Client

client = Client()


class TestHomepage(TestCase):

    def test_index_page(self):
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'Bad status code')
        self.assert_(isinstance(response, HttpResponse), 'Bad response type')
        self.assertEqual(
            response.headers['content-type'], 'text/html; charset=utf-8', 'Bad content type'
        )

        response_ = client.get('/index/')
        self.assertEqual(response_.status_code, 200, 'Bad status code')
        self.assert_(isinstance(response_, HttpResponse), 'Bad response type')
        self.assertEqual(
            response_.headers['content-type'], 'text/html; charset=utf-8', 'Bad content type'
        )
        self.assertEqual(client.get('/index').status_code, 301, 'Bad status code')

        self.assertEqual(
            response.content, response_.content,
            'Page with path "/" and page with path "/index" are unequal'
        )


class TestPriceList(TestCase):

    def test_pricelist_page(self):
        response = client.get('/price-list/')
        self.assertEqual(response.status_code, 200, 'Bad status code')
        self.assert_(isinstance(response, FileResponse))
        self.assertEqual(response.headers['content-type'], 'application/pdf', 'Bad content type')
        self.assertEqual(client.get('/price-list').status_code, 301, 'Bad status code')

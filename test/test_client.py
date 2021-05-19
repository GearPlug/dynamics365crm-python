import os
from unittest import TestCase
from urllib.parse import urlparse, parse_qs
from dynamics365crm.client import Client


class Dynamics365CRMTestCases(TestCase):
    def setUp(self):
        self.client_id = os.environ.get("CLIENT_ID")
        self.client_secret = os.environ.get("CLIENT_SECRET")
        self.token = os.environ.get("ACCESS_TOKEN")
        self.redirect_url = os.environ.get("REDIRECT_URL")
        self.resource = os.environ.get("RESOURCE")
        self.client = Client(
            client_id=self.client_id, client_secret=self.client_secret, token=self.token
        )

    def test_oauth_access(self):
        url = self.client.url_petition(self.redirect_url, self.resource)
        self.assertIsInstance(url, str)
        o = urlparse(url)
        query = parse_qs(o.query)
        self.assertIn("client_id", query)
        self.assertEqual(query["client_id"][0], self.client_id)
        self.assertIn("redirect_uri", query)
        self.assertEqual(query["redirect_uri"][0], self.redirect_url)

    def test_get_data(self):
        response = self.client.get_data(
            type="contacts",
            select="fullname, emailaddress1, createdon",
            orderby="createdon desc",
            top="1",
        )
        self.assertIsInstance(response, dict)

    def test_create_data(self):
        response = self.client.create_data(
            type="contacts",
            firstname="NAME",
            lastname="LASTNAME",
            middlename="MIDDLENAME",
            emailaddress1="EMAIL@EMAIL.COM",
        )
        print(response)
        self.assertIsInstance(response, bool)

from django.test import TestCase, Client
from django.urls import reverse

class APIListViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('document-list')
        self.result = self.client.get(self.url)

    def test_list_documents_is_ok(self):

        # import ipdb;ipdb.set_trace()
        assert self.result.status_code == 200


class APICreateViewTestCase(TestCase):
    pass

class APIDetailTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        # create a document
        # data = {..}
        # document = Document.objects.create(**data)
        # get the url:
        # self.url = reverse('document-detail', args=(document.id,))
        # self.result = self.client.get(self.url)

    def test_list_documents_is_ok(self):
        pass
        # import ipdb;ipdb.set_trace()
        # assert self.result.status_code == 200

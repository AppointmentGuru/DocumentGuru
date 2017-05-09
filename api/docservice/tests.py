from django.test import TestCase, Client
from django.urls import reverse
from .models import Document
from PIL import Image

import tempfile

class APIListViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('document-list')
        self.result = self.client.get(self.url)

    def test_list_documents_is_ok(self):

        # import ipdb;ipdb.set_trace()
        assert self.result.status_code == 200


class APICreateViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('document-list')

        image = Image.new('RGB', (100, 100))
        self.file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(self.file, 'jpeg')

        with open(self.file.name, 'rb') as data:
            self.result = self.client.post(self.url, {"image": data, "name": 'test-document'}, format='multipart')

    def test_create_document_is_ok(self):
        assert self.result.status_code == 201

    def test_assert_file_is_uploaded(self):
        assert Document.objects.count() == 1, \
            'Expected a new document to have been created. There are: {} document/s'.format(Document.objects.count())

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

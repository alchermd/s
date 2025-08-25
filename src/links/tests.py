from django.http import Http404
from django.test import TestCase, RequestFactory

from links.models import Link
from links.views import link_detail


class TestLinkDetails(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_existing_link_redirects(self):
        link = Link.objects.create(url="https://example.com")
        fake_request = self.factory.request()
        response = link_detail(fake_request, link.public_id)
        assert 302 == response.status_code
        assert "https://example.com" == response.url
        assert 1 == link.clicks.count()

    def test_noexistent_link_404s(self):
        fake_request = self.factory.request()
        with self.assertRaises(Http404):
            link_detail(fake_request, "nonexistent")

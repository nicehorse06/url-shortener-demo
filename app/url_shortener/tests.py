from django.test import TestCase
from mysite.settings import HOSTNAME
from .models import UrlRecord

# 測試的網址，可依據django起的環境更改
test_url = 'http://127.0.0.1:8000/'

class UrlRecordTestCase(TestCase):
    def setUp(self):
        pass

    def test_shortener_url_check(self):
        """確認生成縮網址的功能"""
        self.assertTrue(UrlRecord.shortener_url(1) == (HOSTNAME + '\\1'))
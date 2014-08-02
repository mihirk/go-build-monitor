import os
import os.path
import shutil

from django.test import TestCase

from logic.http_utils import create_file, download_cctray_xml, get_cctray_xml
import httpretty


class HTTPUtilsTest(TestCase):
    def setUp(self):
        if (os.path.isdir("test")):
            pass
        else:
            os.mkdir("test")
        test_xml = open('test_build.xml', 'r')
        self.xml_content = test_xml.read()

    def tearDown(self):
        shutil.rmtree('test', True)

    def test_create_file(self):
        create_file("test/test_file_name", "test_content")
        test_handle = open("test/test_file_name", 'r')
        content = test_handle.read()
        self.assertIsNotNone(test_handle)
        self.assertEqual("test_content", content)

    def test_error_handling_for_non_xml_url(self):
        error = download_cctray_xml(url="someurl", username=None, password=None, file_name=None)
        self.assertEqual("Give the cctray url ending with .xml", error)

    def test_cctray_download(self):
        httpretty.enable()
        httpretty.register_uri(httpretty.GET, "http://cctray.com/xml",
                               body=self.xml_content)
        cctray = get_cctray_xml(url="http://cctray.com/xml", username=None, password=None)
        self.assertEqual(self.xml_content, cctray.read())
        httpretty.disable()
        httpretty.reset()

    def test_cctray_download_with_password(self):
        httpretty.enable()
        httpretty.register_uri(httpretty.GET, "http://cctray.com/xml",
                               body=self.xml_content)
        cctray = get_cctray_xml(url="http://cctray.com/xml", username="something", password="something")
        self.assertEqual(self.xml_content, cctray.read())
        httpretty.disable()
        httpretty.reset()

    def test_download_success(self):
        httpretty.enable()
        httpretty.register_uri(httpretty.GET, "http://cctray.com/.xml",
                               body=self.xml_content)
        status = download_cctray_xml("http://cctray.com/.xml", username=None, password=None,
                                     file_name="test/download_file_name")
        self.assertEqual("Success", status)
        self.assertTrue(os.path.isfile("test/download_file_name"))
        httpretty.disable()
        httpretty.reset()
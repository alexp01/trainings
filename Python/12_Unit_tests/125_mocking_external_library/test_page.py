from page import PageRequester
from unittest import TestCase
from unittest.mock import patch

class TestPageRequester(TestCase):
    def setUp(self):
        self.page = PageRequester('https://google.com')

    def test_make_request(self): # we do not need to test the get response validity but the fact that we can do a get and have a response
        with patch('requests.get') as mocked_get: # this will replace all response.get with a moccked response
            self.page.get()
            mocked_get.assert_called()

    def test_content_returned(self): # now we can also test the returned content, but still with a mocked response.
        class FakeResponse: # we need to declare a fix mocked response, as the default mocked one is random
            def __init__(self):
                self.content = 'Hello'

        with patch('requests.get', return_value=FakeResponse()) as mocked_get:
            result = self.page.get()
            self.assertEqual(result, 'Hello')
from django.test import TestCase

class SampleTestCase(TestCase):
    def setUp(self):
        pass

    def test_twenty_six(self):
        """Test"""
        self.assertEqual(26, 26)

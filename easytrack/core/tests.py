from django.test import TestCase
from core.models import Contact
class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(first_name="Stephen", last_name = "Castle")

    def test_contact_unicode_is_fullname(self):
        """Test that a contact is created"""
        contact = Contact.objects.get(first_name="Stephen")
        self.assertEqual(contact.__unicode__(), "Stephen Castle")

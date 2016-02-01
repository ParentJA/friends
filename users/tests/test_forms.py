# Django imports...
from django.test import TestCase

# Local imports...
from ..forms import ProfileForm

__author__ = 'Jason Parent'


class ProfileFormTest(TestCase):
    def test_form_has_required_fields(self):
        form = ProfileForm()

        self.assertIn('id="id_photo"', form.as_p())

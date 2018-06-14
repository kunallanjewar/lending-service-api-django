from django.test import TestCase
from .models import LendingRecord

class ModelTestCase(TestCase):
    """Class defines test suite for out model"""

    def set_up(self):
        self.name = "lending record"
        self.lending_record = LendingRecord(name=self.name)

    def test_model_can_create_a_table_in_db(self):
        old_count = LendingRecord.objects.count()
        self.lending_record.save()
        new_count = LendingRecord.objects.count()
        self.assertNotEqual(old_count, new_count)

import json
import os
import unittest

from termutils.calendar import get_date_labels, labeled_calendar

testpath = os.path.dirname(__file__)


class Test(unittest.TestCase):
    """ Test main module """

    def read_data(self):
        with open(os.path.join(testpath, 'data.json')) as f:
            data = json.loads(f.read())
        return data

    def test_get_date_labels(self):
        items = self.read_data()
        results = get_date_labels(items, 'platform', date_field='datetime')
        assert(len(results) == 2)
        print(results)

    def test_calendar(self):
        items = self.read_data()
        labels = get_date_labels(items, 'platform', date_field='datetime')
        print(labeled_calendar(labels))

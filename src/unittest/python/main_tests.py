import unittest

from main import getPrediction

class mainTest(unittest.TestCase):
    def test_get(self):
        self.assertEquals(getPrediction("Un.png"),"Tuberculosis")
    
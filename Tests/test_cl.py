import unittest, subprocess
from ProductionCode.helper import *

class ProjectMethodsTests(unittest.TestCase):
    def test_is_disaster(self):
        test1 = is_disaster("tornado")
        self.assertEqual(test1, True)

        edgetest1 = is_disaster("TORNADO")
        self.assertEqual(edgetest1, True)

        test2 = is_disaster("United States")
        self.assertEqual(test2, False)

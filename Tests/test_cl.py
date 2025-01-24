import unittest, subprocess

from ProductionCode.helper import *

class ProjectMethodsTests(unittest.TestCase):
    def test_is_disaster(self):
        test1 = is_disaster("Rice")
        self.assertEqual(test1, "True")

        edgetest1 = is_disaster("rIcE")
        self.assertEqual(edgetest1, "True")

        test2 = is_disaster("Potato")
        self.assertEqual(test2, "False")

        edgetest2 = is_disaster(4)
        self.assertEqual(edgetest2, "False")
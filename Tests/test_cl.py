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
        
##



    def test_are_disasters(self):
        test1 = is_disaster("tornado,hurricane,wildfire")
        self.assertEqual(test1, True)

        test2 = is_disaster("tornado,hurricane,alien invasion")
        self.assertEqual(test2, False)

        edgetest1 = is_disaster("TORNADO,HURRICANE")
        self.assertEqual(edgetest1, True)

    def test_is_us_county(self):
        test1 = is_us_county("Los Angeles, CA")
        self.assertEqual(test1, True)

        test2 = is_us_county("Atlantis")
        self.assertEqual(test2, False)

        edgetest1 = is_us_county("LOS ANGELES, CA")
        self.assertEqual(edgetest1, True)

    def test_get_top_five(self):
        result = get_top_five("Los Angeles")
        self.assertEqual(len(result), 5)  # Ensure exactly 5 disasters returned

        for disaster, rating in result.items():
            self.assertIsInstance(disaster, str)
            self.assertIsInstance(rating, str)

        with self.assertRaises(Exception):
            get_top_five("Atlantis")

    def test_partial_disaster_input(self):
        test1 = is_disaster("tor")
        self.assertEqual(test1, False)

        test2 = is_disaster("hurri")
        self.assertEqual(test2, False)

    def test_disaster_with_special_characters(self):
        test1 = is_disaster("tornado@")
        self.assertEqual(test1, False)

        test2 = is_disaster("wildfire#")
        self.assertEqual(test2, False)

    def test_county_with_special_characters(self):
        test1 = is_us_county("Los Angeles@")
        self.assertEqual(test1, False)

        test2 = is_us_county("Atlantis#")
        self.assertEqual(test2, False)

    def test_large_county_name(self):
        test1 = is_us_county("ThisIsAVeryLongCountyNameThatDoesNotExist")
        self.assertEqual(test1, False)

        test2 = is_us_county("LA")
        self.assertEqual(test2, False)

    def test_valid_disaster_list(self):
        test1 = is_disaster("tornado,hurricane,earthquake")
        self.assertEqual(test1, True)

        test2 = is_disaster("tornado hurricane earthquake")
        self.assertEqual(test2, False)

        test3 = is_disaster("tornado,hurricane,alien")
        self.assertEqual(test3, False)
    

if __name__ == "__main__":
    unittest.main()
import unittest, subprocess
from ProductionCode.helper import *
from ProductionCode.datasource import DataSource

test = DataSource()
test.connect()

class ProjectMethodsTests(unittest.TestCase):
    def test_is_disaster(self):
        ''' Argument: instance of ProjectMethodsTests
        Tests to see if is_disaster correctly finds if a singular entry is a disaster in the dataset
        '''
        test1 = is_disaster("tornado")
        self.assertEqual(test1, True)

        test2 = is_disaster("United States")
        self.assertEqual(test2, False)

        edgetest1 = is_disaster("TORNADO")
        self.assertEqual(edgetest1, True)

        edgetest2 = is_disaster(5)
        self.assertEqual(edgetest2, False)


    def test_are_disasters(self):
        '''Argument: instance of ProjectMethodsTests
        Tests to see if is_disaster correctly finds if every entry is a disaster in the dataset and are separated by commas
        '''
        test1 = is_disaster("tornado,hurricane,wildfire")
        self.assertEqual(test1, True)

        test2 = is_disaster("tornado,hurricane,alien invasion")
        self.assertEqual(test2, False)

        edgetest1 = is_disaster("TORNADO,HURRICANE")
        self.assertEqual(edgetest1, True)

        edgetest2 = is_disaster("tornado hurricane earthquake")
        self.assertEqual(edgetest2, False)

    def test_is_us_county(self):
        '''Argument: instance of ProjectMethodsTests
        Tests to see if is_us_county correctly determines if the inputted county is a county in the United States
        '''
        test1 = test.is_valid_us_county("Los Angeles", "CA")
        self.assertEqual(test1, True)

        test2 = test.is_valid_us_county("Atlantis", "BH")
        self.assertEqual(test2, False)

        edgetest1 = test.is_valid_us_county("LOS ANGELES", "CA")
        self.assertEqual(edgetest1, True)

    def test_get_top_five(self):
        '''Argument: instance of ProjectMethodsTests
        Tests to see if get_top_five correctly returns the five disasters that a county is most at risk of experiencing 
        '''
        countydata = test.getCountyRow("Los Angeles", "CA")
        result = get_top_five(countydata)
        self.assertEqual(len(result), 5)  # Ensure exactly 5 disasters returned

        for disaster, rating in result.items():
            self.assertIsInstance(disaster, str)
            self.assertIsInstance(rating, str)

        with self.assertRaises(Exception):
            test.getCountyRow("Atlantis")

    def test_partial_disaster_input(self):
        '''Argument: instance of ProjectMethodsTests
        Tests to ensure that is_disaster correctly determines that incomplete disasters are not valid inputs
        '''
        test1 = is_disaster("tor")
        self.assertEqual(test1, False)

        test2 = is_disaster("hurri")
        self.assertEqual(test2, False)

    def test_disaster_with_special_characters(self):
        '''Argument: instance of ProjectMethodsTests
        Tests to ensure that is_disaster correctly determines that names with special characters are considered invalid
        '''
        test1 = is_disaster("tornado@")
        self.assertEqual(test1, False)

        test2 = is_disaster("wildfire#")
        self.assertEqual(test2, False)

    def test_county_with_special_characters(self):
        '''Argument: instance of ProjectMethodsTests
        Tests to ensure that is_us_county correctly determines that names with special characters are considered invalid
        '''
        test1 = test.is_valid_us_county("Los Angeles@", "CA")
        self.assertEqual(test1, False)

        test2 = test.is_valid_us_county("Atlantis#", "BH")
        self.assertEqual(test2, False)
    
    def test_main(self):
        '''Argument: instance of ProjectMethodsTests
        Tests main to ensure that the correct output is produced when input is correct or that a Usage statement is printed when input is incorrect 
        '''
        test1 = subprocess.Popen(['python3', 'command_line.py', '--disaster', 'tornado', '--county', 'Rice, MN'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = test1.communicate()
        self.assertEqual(output.strip(), "{'tornado': 'Relatively Moderate'}")
        test1.terminate()

        test2 = subprocess.Popen(['python3', 'command_line.py', '--disaster', 'tornado', '--county', 'Rice'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = test2.communicate()
        self.assertEqual(output.strip(), 'Not a valid county. Please ensure the county is formatted as <county>, <stateabbrv> and try again')
        test2.terminate()

        test3 = subprocess.Popen(['python3', 'command_line.py', '--disaster', 'torn', '--county', 'Rice, MN'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = test3.communicate()
        self.assertEqual(output.strip(), 'At least one disaster is invalid. Please check spelling and try again')
        test3.terminate()

        test4 = subprocess.Popen(['python3', 'command_line.py', '--top5', 'Rice, MN'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = test4.communicate()
        self.assertEqual(output.strip(), "{'Winter Weather': 'Relatively High', 'Hail': 'Relatively High', 'Tornado': 'Relatively Moderate', 'Strong Wind': 'Relatively Moderate', 'Heat Wave': 'Relatively Moderate'}")
        test4.terminate()

        test5 = subprocess.Popen(['python3', 'command_line.py', '--top5', 'Rice'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = test5.communicate()
        self.assertEqual(output.strip(), 'Not a valid county. Please ensure the county is formatted as <county>, <stateabbrv> and try again')
        test5.terminate()

if __name__ == "__main__":
    unittest.main()
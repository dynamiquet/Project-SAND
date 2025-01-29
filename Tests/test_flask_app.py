from flask_app import *
import unittest

class TestSANDPage(unittest.TestCase):
   def test_homepage(self):
      ''' Argument: instance of TestSANDPage
        Tests to see if base route leads user to homepage with correct output
        '''
      self.app = app.test_client()
      response = self.app.get('/', follow_redirects=True)

      self.assertIn(b'Welcome to the homepage for Project S.A.N.D', response.data)

   def test_check_valid_disasters_and_county(self):
      ''' Argument: instance of TestSANDPage
        Tests to see if function correctly returns appropriate boolean for inputs
        '''
      ValidDisaster = "Earthquake"
      ValidDisasters = "Tornado, Earthquake, Hurricane"
      InvalidDisaster = "Potato Weather"
      ValidCounty = "Los Angeles, CA"
      InvalidCounty = "Potato, Kingdom"

      # Should be safe
      test1 = check_valid_disasters_and_county(ValidDisaster, ValidCounty)
      self.assertEqual(test1, True)

      test2 = check_valid_disasters_and_county(ValidDisasters, ValidCounty)
      self.assertEqual(test2, True)

      # Should be rejected
      test3 = check_valid_disasters_and_county(InvalidDisaster, ValidCounty)
      self.assertEqual(test3, False)

      test4 = check_valid_disasters_and_county(ValidDisasters, InvalidCounty)
      self.assertEqual(test4, False)

   def test_disaster_county_pages(self):
      ''' Argument: instance of TestSANDPage
        Tests to see if unique routes lead to correct pages for both correct and incorrect arguments
        '''
      self.app = app.test_client()

      test1 = self.app.get('/Earthquake/Los Angeles,CA', follow_redirects=True)
      self.assertEqual(b'{"Earthquake":"Very High"}\n', test1.data)

      test2 = self.app.get('/Earthquake,Tornado/Los Angeles,CA', follow_redirects=True)
      self.assertEqual(b'{"Earthquake":"Very High","Tornado":"Relatively High"}\n', test2.data)

      Edgetest1 = self.app.get('/Earthquake,Tornado/Los Angeles', follow_redirects=True)
      self.assertEqual(b'Either your county or disaster are not valid inputs. Please check homepage to see correct usage.', Edgetest1.data)

      Edgetest2 = self.app.get('/Earthquake/Rice,MN/POTATOES', follow_redirects=True)
      self.assertEqual(b'Page not found. Please check homepage to see correct browser argument inputs! Thank you!', Edgetest2.data)

   def test_top5_pages(self):
      ''' Argument: instance of TestSANDPage
        Tests to see if unique routes lead to correct pages for both correct and incorrect arguments
        '''
      self.app = app.test_client()

      test1 = self.app.get('/top5/Los Angeles,CA', follow_redirects=True)
      self.assertEqual(b'{"Earthquake":"Very High","Landslide":"Relatively High","Lightning":"Relatively High","Tornado":"Relatively High","Wildfire":"Very High"}\n', test1.data)

      Edgetest1 = self.app.get('/top5/LosAngel', follow_redirects=True)
      self.assertEqual(b'Either your county or disaster are not valid inputs. Please check homepage to see correct usage.', Edgetest1.data)

      Edgetest2 = self.app.get('/top100/', follow_redirects=True)
      self.assertEqual(b'Page not found. Please check homepage to see correct browser argument inputs! Thank you!', Edgetest2.data)
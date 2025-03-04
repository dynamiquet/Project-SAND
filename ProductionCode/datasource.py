import psycopg2
import ProductionCode.psqlConfig as config
from ProductionCode.helper import *

class DataSource:
    
    def __init__(self):
        '''
        Constructor that initiates connection to database
        '''
        self.connection = self.connect()

    def connect(self):
        '''
        Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object.
        '''

        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def is_valid_us_county(self, county, state):
        '''Arguments: county (string), state (string)
        Returns: Boolean
        Checks to see if the inputted county exists by running a SQL query to scan for a row in the database that has the inputted county and state 
        '''

        try:
            cursor = self.connection.cursor()

            query = f"SELECT EXISTS (SELECT 1 FROM county_and_riskvalues WHERE COUNTY = %s AND STATEABBRV = %s);"

            # .title() accounts for counties that are not inputted with only the first letter capitalized
            cursor.execute(query, (county.title(), state,))

            result = cursor.fetchall()

            if (result[0][0] == True):
                return True
            else:
                return False
        except Exception as e:
            print("Something went wrong when executing the query:", e)

            return None
    
    def get_risk_values_by_county(self, disasters, county, state):
        ''' 
        Arguments: disasters (string), county (string), state (string)
        Executes a SQL query by taking in the disasters list which are the columns of the database and retrieving the risk values for the specified US county which are then
        displayed 
        '''
        try:
            if (self.is_valid_us_county(county, state) == True and is_disaster(disasters) == True):
                cursor = self.connection.cursor()

                query = f"SELECT {disasters} FROM county_and_riskvalues WHERE COUNTY = %s AND STATEABBRV = %s;"

                cursor.execute(query, (county, state,))

                listofriskvalues = list(cursor.fetchall()[0])

                disasterslist = split_and_strip_strings(disasters)

                disasterriskdictionary = get_disaster_risk_dict(disasterslist, listofriskvalues)
                
                return disasterriskdictionary
            else:
                return "Invalid county and/or invalid disaster(s)"
        except Exception as e:
            print("Something went wrong when executing the query:", e)

            return None
    
    def get_county_row(self, county, state):
        ''' 
        Arguments: county (string), state (string)
        Returns: the entire row of a county in the database
        Used to get a specific county's data to then be able to perform operations on it
        '''
        try:
            if (self.is_valid_us_county(county, state) == True):
                cursor = self.connection.cursor()

                query = f"SELECT * FROM county_and_riskvalues WHERE COUNTY = %s AND STATEABBRV = %s;"

                cursor.execute(query, (county, state,))

                countyrowdata = list(cursor.fetchall()[0])
                
                return countyrowdata
            else:
                return "Invalid county"
        except Exception as e:
            print("Something went wrong when executing the query:", e)

            return None

        

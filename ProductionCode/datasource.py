import psycopg2
import ProductionCode.psqlConfig as config

class DataSource:

    def __init__(self):
        '''Constructor that initiates connection to database'''
        self.connection = self.connect()

    def connect(self):
        '''Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object.'''

        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
    
    def getRiskValuesbyCounty(self, disasters, county, state):
        ''' Arguments: disasters (string), county (string), state (string)
        Executes a SQL query by taking in the disasters list which are the columns of the database and retrieving the risk values for the specified US county which are then
        displayed 
        '''
        try:
            cursor = self.connection.cursor()

            query = f"SELECT {disasters} FROM county_and_riskvalues WHERE COUNTY = %s AND STATEABBRV = %s;"

            cursor.execute(query, (county, state,))

            listofriskvalues = cursor.fetchall()

            # Removes the [] 
            print(listofriskvalues[0])
        except Exception as e:
            print("Something went wrong when executing the query:", e)

            return None
        

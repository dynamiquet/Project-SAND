from flask import Flask
from ProductionCode.helper import *

app = Flask(__name__)

@app.route('/')
def homepage():
    '''Arguments: None
    Return: String
    Purpose: To provide instructions on how to use homepage'''

    message = '''Welcome to the homepage for Project S.A.N.D.!<br> <br> 
    In order to use this website concatenate arguments into the browser with ' / ' followed by either: 
    <br><br> Usage One: &lt name of disaster(s) seperated by commas &gt / &lt name of US county, State abbreviation &gt <br>
    Example: (existing url)/Tornado,Earthquake/Los Angeles,CA <br> <br>
    This returns the hazard rating for the type of disaster(s) in the given county as recorded by FEMA's dataset<br><br>
    Usage Two: top5/ &lt name of US county, State abbreviation &gt <br>
    Example: (existing url)/top5/Rice,MN <br> <br>
    This returns the top five most hazardous disaster's in a given county
    '''
    return message
    
ErrorMessage = "Either your county or disaster are not valid inputs. Please check homepage to see correct usage."

def check_valid_disasters_and_county(disaster, county):
    '''Arguments: String of disaster(s), String of county
    Return: Boolean
    Purpose: To check if given disasters and county are valid'''

    return (is_disaster(disaster) and is_us_county(county))

@app.route('/<disaster>/<county>', strict_slashes = False)
def get_valid_county_and_disaster(disaster, county):
    '''Arguments: String of disaster(s), String of county
    Return: List of disaster's
    Purpose: To get disaster's hazard ratings in a county'''

    if (check_valid_disasters_and_county(disaster, county)):
        return get_disaster_risk(disaster, county)
    
    return ErrorMessage
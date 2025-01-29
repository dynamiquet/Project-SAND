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

@app.route('/disasters/<disasters>/county/<county>', strict_slashes = False)
def get_disaster_risk_flsk(disasters, county):
    '''Argument(s): disasters (string), county (string)
    Returns the dictionary with every inputted disaster and their respective risk values for the specific county
    '''

    if (is_disaster(disasters) == True and is_us_county(county) == True):
        return get_disaster_risk(disasters, county)
    else:
        return "At least one disaster and/or the county are not valid. Please check spelling and try again. For information on formatting, check the homepage."
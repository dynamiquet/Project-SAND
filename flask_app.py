from flask import Flask, render_template, request
from ProductionCode.helper import *
from ProductionCode.datasource import DataSource
# comment
app = Flask(__name__)
test = DataSource()
test.connect()

@app.errorhandler(404)
def page_not_found(e):
    '''Argument(s): 404 error
    Displays a usage statement to the user if what follows the URL is formatted incorrectly
    '''
    return render_template('displayerror.html')

@app.errorhandler(500)
def python_bug(e):
   '''Arguments: None
    Return: String of instructions
    Purpose: In case of developer error, directs users back to homepage'''
   #"Sorry for the error, we have a bug in our code! Please go back to the homepage!" 
   return render_template('displayerror.html')

@app.route('/prevhome')
def display_prev_homepage():
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

@app.route('/<disaster>/<county>', strict_slashes = False)
def get_valid_county_and_disaster(disaster, county):
    '''Arguments: String of disaster(s), String of county
    Return: List of disaster's
    Purpose: To get disaster's hazard ratings in a county'''

    county_list = split_and_strip_strings(county)

    if (is_formatted_county_and_state(county_list) == False):
        return ErrorMessage
    
    county_name = county_list[0]
    state_abbrv = county_list[1]

    if (test.is_valid_us_county(county_name, state_abbrv) and is_disaster(disaster)):
        return test.getRiskValuesbyCounty(disaster, county_name, state_abbrv)
    
    return ErrorMessage

@app.route('/top5/<county>', strict_slashes = False)
def get_top5_disasters_for_county(county):
    '''Arguments: String of county
    Return: List of disaster's and ratings
    Purpose: To get top 5 hazardous disasters in a county'''

    county_list = split_and_strip_strings(county)

    if (is_formatted_county_and_state(county_list) == False):
        return ErrorMessage
    
    county_name = county_list[0]
    state_abbrv = county_list[1]
    
    if (test.is_valid_us_county(county_name, state_abbrv)):
        county_data = test.getCountyRow(county_name, state_abbrv)
        return get_top_five(county_data)
    
    return ErrorMessage


# New URLs 
@app.route('/displaycountydata')
def display_county_disaster_data():
    requested_county = str(request.args['county'])
    requested_state = str(request.args['state'])
    requested_disasters_list = str(request.args.getlist('hiddenSelectedDisaster'))[2:-2]
    risk_values_for_disasters_dictionary = test.getRiskValuesbyCounty(requested_disasters_list, requested_county, requested_state)
    return render_template('displaydata.html', results = risk_values_for_disasters_dictionary, state = requested_state, county=requested_county, data=risk_values_for_disasters_dictionary)

@app.route('/top5')
def get_top5_risk_values_for_county():
    requested_state = request.args['stateabbrv']
    requested_county = request.args['county']

    county_data = test.getCountyRow(requested_county, requested_state)

    return render_template("displaytop5data.html", county=requested_county, state=requested_state, data=get_top_five(county_data))

@app.route('/top5page')
def display_top5_page():
    return render_template("top5.html")

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/currlocation')
def deadhomepage():
    return render_template('getlocation.html')

@app.route('/resources')
def deadnews():
    return render_template("resources.html")

@app.route('/about')
def deadabout():
    return "Page describing who we are and what our mission is."

if __name__ == '__main__':
    app.run()

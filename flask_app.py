from flask import Flask, render_template, request
from ProductionCode.helper import *
from ProductionCode.datasource import DataSource

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
    Purpose: In case of developer error, directs users back to homepage
    '''
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
    
error_message = "Either your county or disaster are not valid inputs. Please check homepage to see correct usage."

@app.route('/<disaster>/<county>', strict_slashes = False)
def get_valid_county_and_disaster(disaster, county):
    '''Arguments: String of disaster(s), String of county
    Return: List of disaster's
    Purpose: To get disaster's hazard ratings in a county'''

    county_list = split_and_strip_strings(county)

    if (is_formatted_county_and_state(county_list) == False):
        return error_message
    
    county_name = county_list[0]
    state_abbrv = county_list[1]

    if (test.is_valid_us_county(county_name, state_abbrv) and is_disaster(disaster)):
        return test.get_risk_values_by_county(disaster, county_name, state_abbrv)
    
    return error_message

@app.route('/top5/<county>', strict_slashes = False)
def get_top5_disasters_for_county(county):
    '''Arguments: String of county
    Return: List of disaster's and ratings
    Purpose: To get top 5 hazardous disasters in a county'''

    county_list = split_and_strip_strings(county)

    if (is_formatted_county_and_state(county_list) == False):
        return error_message
    
    county_name = county_list[0]
    state_abbrv = county_list[1]
    
    if (test.is_valid_us_county(county_name, state_abbrv)):
        county_data = test.get_county_row(county_name, state_abbrv)
        return get_top_five(county_data)
    
    return error_message


# New URLs 
@app.route('/displaycountydata')
def display_county_disaster_data():
    requested_county = request.args['county']
    requested_state = request.args['state']
    requested_disasters_list = str(request.args.getlist('hiddenSelectedDisaster'))[2:-2]

    risk_values_for_disasters_dictionary = test.get_risk_values_by_county(requested_disasters_list, requested_county, requested_state)

    updated_risk_values_for_disasters_dictionary = pluralize_disaster_names(risk_values_for_disasters_dictionary)

    sorted_risk_values_dictionary = sort_risk_ratings_of_dictionary(updated_risk_values_for_disasters_dictionary)

    print(sorted_risk_values_dictionary)
    
    return render_template('displaydata.html', state = requested_state, county=requested_county, data=sorted_risk_values_dictionary)

@app.route('/top5')
def get_top5_risk_values_for_county():
    requested_state = request.args['state']
    requested_county = request.args['county']

    county_data = test.get_county_row(requested_county, requested_state)

    top5_risk_values_dictionary = get_top_five(county_data)

    updated_risk_values = pluralize_disaster_names(top5_risk_values_dictionary)

    return render_template("displaytop5data.html", county=requested_county, state=requested_state, data=updated_risk_values)

@app.route('/top5page')
def display_top5_page():
    return render_template("top5.html")

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/currlocation')
def get_current_location_page():
    return render_template('getlocation.html')

@app.route('/resources')
def display_resources_page():
    return render_template("resources.html")

@app.route('/about')
def display_about_me_page():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()

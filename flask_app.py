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
    return "Page not found: Please ensure you follow the URL with: /&ltdisasters&gt/&ltcounty, state abbr.&gt or /&ltrow&gt/&ltcolumn&gt"

@app.errorhandler(500)
def python_bug(e):
   '''Arguments: None
    Return: String of instructions
    Purpose: In case of developer error, directs users back to homepage'''
   return "Sorry for the error, we have a bug in our code! Please go back to the homepage!" 

@app.route('/prevhome')
def prevhomepage():
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

    countylist = split_and_strip_strings(county)

    if (is_formatted_county_and_state(countylist) == False):
        return ErrorMessage
    
    countyname = countylist[0]
    stateabbrv = countylist[1]

    if (test.is_valid_us_county(countyname, stateabbrv) and is_disaster(disaster)):
        return test.getRiskValuesbyCounty(disaster, countyname, stateabbrv)
    
    return ErrorMessage

@app.route('/top5/<county>', strict_slashes = False)
def get_valid_top5_county(county):
    '''Arguments: String of county
    Return: List of disaster's and ratings
    Purpose: To get top 5 hazardous disasters in a county'''

    countylist = split_and_strip_strings(county)

    if (is_formatted_county_and_state(countylist) == False):
        return ErrorMessage
    
    countyname = countylist[0]
    stateabbrv = countylist[1]
    
    if (test.is_valid_us_county(countyname, stateabbrv)):
        countydata = test.getCountyRow(countyname, stateabbrv)
        return get_top_five(countydata)
    
    return ErrorMessage

@app.route('/displaydata')
def display_data():
    county = str(request.args['county'])
    state = str(request.args['state'])
    disasters = str(request.args.getlist('hiddenSelectedDisaster'))[2:-2]
    data = get_limited_county_and_disasters(county, state, disasters)
    print(data)
    return render_template('displaydata.html', results = data, state = state, county=county)

@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5138)

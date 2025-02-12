import csv, sys

def is_disaster(disasters_str):
    ''' 
    Arguments: Takes in user string of disaster(s)
    Returns: True or False
    Purpose: Checks to see if each disaster in the list inputted is a disaster in the data; takes care of singular entries and list of entries
    '''
    # Checks if input is a string
    if (not isinstance(disasters_str, str)):
        return False
    
    valid_disaster_list = return_alphabetical_disaster_list()

    split_disasters = split_and_strip_strings(disasters_str)

    for disaster in split_disasters:
        if disaster.lower() not in valid_disaster_list:
            return False
    
    return True

def is_us_county(county):
    ''' 
    Arguments: Takes in a county as a string
    Returns: True or False
    Purpose: Checks to see if county inputted is in the US and accounts for counties that share the same name
    '''
    county_and_state = split_and_strip_strings(county)

    # Checking to ensure that the input is formatted correctly
    if (len(county_and_state) != 2):
        return False

    return validate_county_in_dataset(county_and_state)

def get_disaster_risk(disasters, county):
    ''' 
    Arguments: Takes in a string of disasters and county
    Returns: A dictionary
    Purpose: Seperates disaster(s) string into list and returns a hazard rating for each disaster
    '''
    target_county_data = get_filtered_county_data(county)

    disasters_list = split_and_strip_strings(disasters)

    userdictionary = get_disaster_risk_helper(disasters_list, target_county_data)
    
    return userdictionary

def get_disaster_risk_helper(disasterlist, countyrow):
    ''' 
    Arguments: String of disasters and a list of hazardous ratings
    Returns: A dictionary
    Purpose: Assigns a hazard rating for each disaster from the specified county's list of data
    '''

    # Each key is a disaster and the value is what column their risk value is in the dataset
    disasterandcolumndict = {"avalanche":0,"coastal flooding":1, "cold wave":2, "drought":3, "earthquake":4, "hail":5, "heat wave":6, "hurricane":7, 
                         "ice storm":8, "landslide":9, "lightning":10, "riverine flooding":11, "strong wind":12, "tornado":13, "tsunami":14, 
                         "volcanic activity":15, "wildfire":16, "winter weather":17}

    dictionary = {}

    for disaster in disasterlist:
        column = disasterandcolumndict[disaster.lower()]
        dictionary.update({disaster : countyrow[column]})

    return dictionary


def get_int_rating(table_rating):
    ''' 
    Arguments: String of a hazard rating
    Returns: A int
    Purpose: Assigns a numerical value for each type of hazard rating for future sorting
    '''

    # Each key is a rating from the dataset and is associated with an integer
    stringratingdict = {"Insufficient Data":0, "Not Applicable":1, "No Rating":2, "Very Low":3, "Relatively Low":4, "Relatively Moderate":5,
                        "Relatively High":6, "Very High":7}
    
    # Convert string rating into an integer for sorting
    if table_rating in stringratingdict:
        int_rating = stringratingdict[table_rating]

    return int_rating

def get_string_rating(int_rating):
    ''' 
    Arguments: A numerical value for a hazard rating
    Returns: A string
    Purpose: Reverts a numerical value for each type of hazard rating for user readability
    '''

    # Each key is an integer and is associated with a rating from the dataset
    intratingdict = {0:"Insufficient Data", 1:"Not Applicable", 2:"No Rating", 3:"Very Low", 4:"Relatively Low", 5:"Relatively Moderate",
                     6:"Relatively High", 7:"Very High"}
    
    # Revert ratings for back into data hazards rating labels
    string_rating = intratingdict[int_rating]

    return string_rating

def get_top_five(countyrow):
    ''' 
    Arguments: Takes in a county as a string
    Returns: A dictionary
    Purpose: Returns the top 5 most hazardous disaster's in a given county
    '''
    sorted_disasters_dict = get_sorted_dangerous_disasters_by_county(countyrow)

    top_5_disasters = get_top_num_items_in_dict(sorted_disasters_dict, 5)

    return top_5_disasters

def split_and_strip_strings(string):
    ''' 
    Arguments: Takes in user string
    Returns: List of split disasters
    Purpose: Cleans up user string for code usability
    '''
    new_split_list = []
    split_string = string.split(',')
    
    for entry in split_string:
        new_split_list.append(entry.lstrip())
    
    return new_split_list

def return_alphabetical_disaster_list():
    ''' 
    Arguments: None
    Returns: List of valid disasters in alphabetical order
    Purpose: Remove clutter in functions requiring list of valid disasters
    '''
    return ["avalanche", "coastal flooding", "cold wave", "drought", "earthquake", "hail",
            "heat wave", "hurricane", "ice storm", "landslide", "lightning", "riverine flooding", 
            "strong wind", "tornado", "tsunami", "volcanic activity", "wildfire", "winter weather"]

def validate_county_in_dataset(county_and_state):
    ''' 
    Arguments: County and state strings in list
    Returns: Boolean
    Purpose: Opens County and Disaster Dataset and validates user county and state
    '''
    with open('Data/County_and_Disasters_only.csv', 'r') as file:
        disasterdata = csv.reader(file)
        for row in disasterdata:
            if str(row[0]).lower() == county_and_state[0].lower() and str(row[1]).lower() == county_and_state[1].lower():
                return True
        return False
    
def get_county_row(county_and_state):
    ''' 
    Arguments: County and state strings in list
    Returns: List of target data
    Purpose: Opens County and Disaster Dataset and retrieves targeted county's row data as a list
    '''
    with open('Data/County_and_Disasters_only.csv', 'r') as file:
        disasterdata = csv.reader(file)
        for row in disasterdata:
            if str(row[0]).lower() == county_and_state[0].lower() and str(row[1]).lower() == county_and_state[1].lower():
                targetcountydata = row[0:]

    return targetcountydata

def remove_county_and_state_columns(data):
    ''' 
    Arguments: List in the form of a row of data from dataset
    Returns: List
    Purpose: Removes the first two columns in a row of data
    '''
    data.pop(0)
    data.pop(0)

def initialize_disaster_rating_dict():
    ''' 
    Arguments: None
    Returns: Dictionary of disasters and ratings
    Purpose: Initializes disaster dictionary with integer ratings set to zero
    '''
    disaster_rating_dict = {
        "Avalanche" : 0, "Coastal Flooding" : 0, "Cold Wave" : 0, "Drought" : 0, "Earthquake" : 0, "Hail" : 0, "Heat Wave" : 0, "Hurricane": 0, 
        "Ice Storm": 0, "Landslide": 0, "Lightning" : 0, "Riverine Flooding" : 0, "Strong Wind" : 0, "Tornado" : 0, "Tsunami" : 0,
        "Volcanic Activity" : 0, "Wildfire" : 0, "Winter Weather" : 0
    }

    return disaster_rating_dict

def disaster_to_int_rating_dict(disaster_dict, county_data):
    ''' 
    Arguments: Disaster dictionary and county data list
    Returns: Void
    Purpose: Converts hazard ratings in county data to numerical values for disaster dict sorting
    '''
    # Variable to keep track of where in list of county data we are at
    county_data_pos = 0

    # Depending on rating, assign numerical value for later sorting
    for disaster in disaster_dict:

        county_disaster_rating = get_int_rating(county_data[county_data_pos])

        disaster_dict.update({disaster : county_disaster_rating})

        county_data_pos += 1

def disaster_to_str_rating_dict(disaster_dict):
    ''' 
    Arguments: Disaster dictionary
    Returns: Void
    Purpose: Converts hazard ratings from numerical values to string hazard ratings
    '''
    # Revert numerical values back to string value for user readability
    for disaster in disaster_dict:

        disaster_string_rating = get_string_rating(disaster_dict.get(disaster))

        disaster_dict.update({disaster : disaster_string_rating})

def get_filtered_county_data(targetcountydata):
    ''' 
    Arguments: String of desired county
    Returns: list of targeted county row data
    Purpose: Returns list of county data with non-hazard rating items removed
    '''
    #county_and_state = split_and_strip_strings(county)

    #targetcountydata = get_county_row(county_and_state)

    remove_county_and_state_columns(targetcountydata)

    return targetcountydata

def get_top_num_items_in_dict(dict, num):
    ''' 
    Arguments: Dictionary and integer
    Returns: Dictionary
    Purpose: Pops the given amount of lowest items in the dictionary
    '''
    dict_length = len(dict)

    for int in range(0, dict_length - num):
        dict.popitem()

    return dict

def get_sorted_dangerous_disasters_by_county(countyrow):
    ''' 
    Arguments: String of County
    Returns: Sorted dictionary
    Purpose: Returns a dictionary with most hazardous disasters in a county in descending order
    '''
    county_data = get_filtered_county_data(countyrow)

    disaster_rating_dict = initialize_disaster_rating_dict()

    disaster_to_int_rating_dict(disaster_rating_dict, county_data)

    # Sort disasters by hazard rating in ascending order
    sorted_disasters_dict = dict(reversed(sorted(disaster_rating_dict.items(), key=lambda item: item[1])))

    disaster_to_str_rating_dict(sorted_disasters_dict)

    return sorted_disasters_dict
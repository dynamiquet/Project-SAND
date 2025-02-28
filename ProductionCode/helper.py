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

def get_int_rating(table_rating):
    ''' 
    Arguments: String of a hazard rating
    Returns: A int
    Purpose: Assigns a numerical value for each type of hazard rating for future sorting
    '''

    # Each key is a rating from the dataset and is associated with an integer value
    string_rating_dict = {"Insufficient Data":0, "Not Applicable":1, "No Rating":2, "Very Low":3, "Relatively Low":4, "Relatively Moderate":5,
                        "Relatively High":6, "Very High":7}
    
    # Convert string rating into an integer for sorting
    if table_rating in string_rating_dict:
        int_rating = string_rating_dict[table_rating]

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
    Arguments: Takes in a countyrowdata as a list
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
    return ["avalanche", "coastalflooding","coastal flooding", "coldwave", "cold wave", "drought", "earthquake", "hail",
            "heatwave", "hurricane", "icestorm", "ice storm", "landslide", "lightning", "riverineflooding", "riverine flooding",  
            "strongwind", "strong wind", "tornado", "tsunami", "volcano", "wildfire",
            "winterweather", "winter weather"]

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
    county_data_position_in_list = 0

    for disaster in disaster_dict:

        county_disaster_rating = get_int_rating(county_data[county_data_position_in_list])

        disaster_dict.update({disaster : county_disaster_rating})

        county_data_position_in_list += 1

def disaster_to_str_rating_dict(disaster_dict):
    ''' 
    Arguments: Disaster dictionary
    Returns: Void
    Purpose: Converts hazard ratings from numerical values to string hazard ratings
    '''
    for disaster in disaster_dict:

        disaster_string_rating = get_string_rating(disaster_dict.get(disaster))

        disaster_dict.update({disaster : disaster_string_rating})

def get_filtered_county_data(target_county_data):
    ''' 
    Arguments: List of county data
    Returns: list of targeted county row data
    Purpose: Returns list of county data with non-hazard rating items removed
    '''

    remove_county_and_state_columns(target_county_data)

    return target_county_data

def get_top_num_items_in_dict(dict, requested_num):
    ''' 
    Arguments: Dictionary and integer
    Returns: Dictionary
    Purpose: Pops the given amount of lowest items in the dictionary
    '''
    dict_length = len(dict)

    for int in range(0, dict_length - requested_num):
        dict.popitem()

    return dict

def get_sorted_dangerous_disasters_by_county(countyrow):
    ''' 
    Arguments: List of county row data
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

def get_disaster_risk_dict(disasters_list, risk_values_list):
    '''
    Arguments: disasterslist (string), riskvalueslist (string)
    Returns: a dictionary
    This function takes in a list of disasters and their associated risk values and creates a dictionary where the key is the disaster and the value
    is its respective risk value
    '''
    disasters_and_risks = {}
    risk_value_list_index = 0

    for disaster in disasters_list:
        disasters_and_risks.update({disaster.lower() : risk_values_list[risk_value_list_index]})
        risk_value_list_index += 1

    return disasters_and_risks

def is_formatted_county_and_state(county_list):
    '''
    Arguments: county_list (string)
    Returns: boolean
    Checks to see if the inputted county is formatted as follows <county>, <state>. The legitimacy of the inputs is checked by is_valid_us_county
    '''

    if (len(county_list) == 2):
        return True
    else:
        return False
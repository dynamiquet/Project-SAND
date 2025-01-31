import csv, sys

def is_disaster(disaster_list):
    ''' 
    Arguments: Takes in a disaster as a string
    Returns: True or False
    Purpose: Checks to see if each disaster in the list inputted is a disaster in the data; takes care of singular entries and list of entries
    '''
    valid_disaster_list = ["avalanche", "coastal flooding", "cold wave", "drought", "earthquake", "hail",
                           "heat wave", "hurricane", "ice storm", "landslide", "lightning", "riverine flooding", 
                           "strong wind", "tornado", "tsunami", "volcanic activity", "wildfire", "winter weather"]
    
    # Checks if input is a string
    if (not isinstance(disaster_list, str)):
        return False
    
    split_list = disaster_list.split(",")

    new_split_list = []
    
    for entry in split_list:
        new_split_list.append(entry.lstrip())

    for disaster in new_split_list:
       
        if disaster.lower() not in valid_disaster_list:
            return False
    
    return True

def is_us_county(county):
    ''' 
    Arguments: Takes in a county as a string
    Returns: True or False
    Purpose: Checks to see if county inputted is in the US and accounts for counties that share the same name
    '''

    # Takes in the string and splits it so that county is the first entry and state is the second entry
    # ['county', 'state']
    split_list = county.split(",")

    new_split_list = []

    for entry in split_list:
        new_split_list.append(entry.lstrip())

    # Checking to ensure that the input is formatted correctly
    if (len(new_split_list) != 2):
        return False
    
    uscounty = new_split_list[0]
    usstate = new_split_list[1]

    with open('Data/County_and_Disasters_only.csv', 'r') as file:
        disasterdata = csv.reader(file)
        for row in disasterdata:
            if str(row[0]).lower() == uscounty.lower() and str(row[1]).lower() == usstate.lower():
                return True

        return False
    
    file.close()

def get_disaster_risk(disasters, county):
    ''' 
    Arguments: Takes in a string of disasters and county
    Returns: A dictionary
    Purpose: Seperates disaster(s) string into list and returns a hazard rating for each disaster
    '''

    # Takes in the string and splits it so that county is the first entry and state is the second entry
    # ['county', 'state']
    split_list = county.split(",")

    new_split_list = []

    for entry in split_list:
        new_split_list.append(entry.lstrip())

    uscounty = new_split_list[0]
    usstate = new_split_list[1]

    # Finds the row in the data with the correct county
    with open('Data/County_and_Disasters_only.csv', 'r') as file:
        disasterdata = csv.reader(file)
        for row in disasterdata:
            if str(row[0]).lower() == uscounty.lower() and str(row[1]).lower() == usstate.lower():
                targetcountydata = row[0:]

    file.close()
    
    # Removes the county column and state abbreviation column to isolate risk ratings
    targetcountydata.pop(0)
    targetcountydata.pop(0)

    # Splitting the inputted disaster string so that each disaster is its own entry in the array
    split_list = disasters.split(",")

    new_split_list = []
    
    for entry in split_list:
        new_split_list.append(entry.lstrip())

    userdictionary = get_disaster_risk_helper(new_split_list, targetcountydata)
    
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
    else:
        print("Error, not a valid rating")

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

def get_top_five(county):
    ''' 
    Arguments: Takes in a county as a string
    Returns: A dictionary
    Purpose: Returns the top 5 most hazardous disaster's in a given county
    '''

    # Takes in the string and splits it so that county is the first entry and state is the second entry
    # ['county', 'state']
    split_list = county.split(",")

    new_split_list = []

    for entry in split_list:
        new_split_list.append(entry.lstrip())

    uscounty = new_split_list[0]
    usstate = new_split_list[1]

    with open('Data/County_and_Disasters_only.csv', 'r') as file:
        disasterdata = csv.reader(file)
        for row_data in disasterdata:
            if str(row_data[0]).lower() == uscounty.lower() and str(row_data[1]).lower() == usstate.lower():
                # Store target county row data
                county_data = row_data[0:]
    file.close()

    # Isolate hazard ratings, remove county and general rating
    county_data.pop(0)
    county_data.pop(0)

    # Variable to keep track of where in list of county data we are at
    county_data_pos = 0

    # Initialize disaster rating dictionary with disasters in order
    disaster_rating_dict = {
        "Avalanche" : 0,
        "Coastal Flooding" : 0,
        "Cold Wave" : 0,
        "Drought" : 0,
        "Earthquake" : 0,
        "Hail" : 0,
        "Heat Wave" : 0,
        "Hurricane": 0,
        "Ice Storm": 0,
        "Landslide": 0,
        "Lightning" : 0,
        "Riverine Flooding" : 0,
        "Strong Wind" : 0,
        "Tornado" : 0,
        "Tsunami" : 0,
        "Volcanic Activity" : 0,
        "Wildfire" : 0,
        "Winter Weather" : 0
    }

    # Depending on rating, assign numerical value for later sorting
    for disaster in disaster_rating_dict:

        county_disaster_rating = get_int_rating(county_data[county_data_pos])

        disaster_rating_dict.update({disaster : county_disaster_rating})

        county_data_pos += 1

    # Sort disasters by hazard rating in ascending order
    sorted_disasters_dict = dict(reversed(sorted(disaster_rating_dict.items(), key=lambda item: item[1])))

    # Revert numerical values back to string value for user readability
    for disaster in sorted_disasters_dict:

        disaster_string_rating = get_string_rating(sorted_disasters_dict.get(disaster))

        sorted_disasters_dict.update({disaster : disaster_string_rating})

    # Pop lowest disasters from dictionary until 5 remain
    for int in range(0,13):
        sorted_disasters_dict.popitem()

    return sorted_disasters_dict

    
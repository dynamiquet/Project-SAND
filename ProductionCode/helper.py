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

    dictionary = {}
    
    for disaster in disasterlist:
        if (disaster.lower() == 'avalanche'):
            dictionary.update({disaster : countyrow[0]})
        elif (disaster.lower() == 'coastal flooding'):
            dictionary.update({disaster : countyrow[1]})
        elif (disaster.lower() == 'cold wave'):
            dictionary.update({disaster : countyrow[2]})
        elif (disaster.lower() == 'drought'):
            dictionary.update({disaster : countyrow[3]})
        elif (disaster.lower() == 'earthquake'):
            dictionary.update({disaster : countyrow[4]})
        elif (disaster.lower() == 'hail'):
            dictionary.update({disaster : countyrow[5]})
        elif (disaster.lower() == 'heat wave'):
            dictionary.update({disaster : countyrow[6]})
        elif (disaster.lower() == 'hurricane'):
            dictionary.update({disaster : countyrow[7]})
        elif (disaster.lower() == 'ice storm'):
            dictionary.update({disaster : countyrow[8]})
        elif (disaster.lower() == 'landslide'):
            dictionary.update({disaster : countyrow[9]})
        elif (disaster.lower() == 'lightning'):
            dictionary.update({disaster : countyrow[10]})
        elif (disaster.lower() == 'riverine flooding'):
            dictionary.update({disaster : countyrow[11]})
        elif (disaster.lower() == 'strong wind'):
            dictionary.update({disaster : countyrow[12]})
        elif (disaster.lower() == 'tornado'):
            dictionary.update({disaster : countyrow[13]})
        elif (disaster.lower() == 'tsunami'):
            dictionary.update({disaster : countyrow[14]})
        elif (disaster.lower() == 'volcanic activity'):
            dictionary.update({disaster : countyrow[15]})
        elif (disaster.lower() == 'wildfire'):
            dictionary.update({disaster : countyrow[16]})
        elif (disaster.lower() == 'winter weather'):
            dictionary.update({disaster : countyrow[17]})

    return dictionary


def get_int_rating(table_rating):
    ''' 
    Arguments: String of a hazard rating
    Returns: A int
    Purpose: Assigns a numerical value for each type of hazard rating for future sorting
    '''
    # Integer ratings for data hazards
    if (table_rating == 'Insufficient Data'):
        int_rating = 0
    elif (table_rating == 'Not Applicable'):
        int_rating = 1
    elif (table_rating == 'No Rating'):
        int_rating = 2
    elif (table_rating == 'Very Low'):
        int_rating = 3
    elif (table_rating == 'Relatively Low'):
        int_rating = 4
    elif (table_rating == 'Relatively Moderate'):
        int_rating = 5
    elif (table_rating == 'Relatively High'):
        int_rating = 6
    elif (table_rating == 'Very High'):
        int_rating = 7
    # Debugging purposes
    else:
        print(table_rating)
        print("Error, not a valid rating")

    return int_rating

def get_string_rating(int_rating):
    ''' 
    Arguments: A numerical value for a hazard rating
    Returns: A string
    Purpose: Reverts a numerical value for each type of hazard rating for user readability
    '''
    # Revert ratings for back into data hazards rating labels
    if (int_rating == 0):
        string_rating = 'Insufficient Data'
    elif (int_rating == 1):
        string_rating = 'Not Applicable'
    elif (int_rating == 2):
        string_rating = 'No Rating'
    elif (int_rating == 3):
        string_rating = 'Very Low'
    elif (int_rating == 4):
        string_rating = 'Relatively Low'
    elif (int_rating == 5):
        string_rating = 'Relatively Moderate'
    elif (int_rating == 6):
        string_rating = 'Relatively High'
    elif (int_rating == 7):
        string_rating = 'Very High'

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

    
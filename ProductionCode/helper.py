import csv, sys

def is_disaster(string):
    ''' Arguments: Takes in a disaster as a string
    Returns: True or False
    Purpose: Checks to see if disaster inputted is a disaster in the data
    '''
    valid_disaster_list = ["avalanche", "coastal flooding", "cold wave", "drought", "earthquake", "hail",
                           "heat wave", "hurricane", "ice storm", "landslide", "lightning", "riverine flooding", 
                           "strong wind", "tornado", "tsunami", "volcanic activity", "wildfire", "winter weather"]
       
    if string.lower() not in valid_disaster_list:
        return False
    else:
        return True

def is_us_county(county):
    ''' Arguments: Takes in a county as a string
    Returns: True or False
    Purpose: Checks to see if county inputted is in the US and thus in the data
    '''
    with open('Data/County_and_Disasters_only.csv', 'r') as file:
        disasterdata = csv.reader(file)
        for row in disasterdata:
            if str(row[0]).lower() == county.lower():
                return True

        return False
    file.close()

def get_int_rating(table_rating):
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
    else:
        print(table_rating)
        print("Error not valid")

    return int_rating

def get_string_rating(int_rating):
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
    with open('Data/County_and_Disasters_only.csv', 'r') as file:
        disasterdata = csv.reader(file)
        for row_data in disasterdata:
            if str(row_data[0]).lower() == county.lower():
                # Store target county row data
                county_data = row_data[0:]

        #Initialize empty dictionary of top five disasters
        top_five_disasters = {}

        # Isolate hazard ratings, remove county and general rating
        county_data.pop(0)
        county_data.pop(0)

        # Variable to keep track of where in list of county data we are at
        county_data_pos = 0

        # Initialize disaster rating dictionary with disasters in order
        disaster_rating_dict = {
            "avalanche" : 0,
            "coastal flooding" : 0,
            "cold wave" : 0,
            "drought" : 0,
            "earthquake" : 0,
            "hail" : 0,
            "heat wave" : 0,
            "hurricane": 0,
            "ice storm": 0,
            "landslide": 0,
            "lightning" : 0,
            "riverine flooding" : 0,
            "strong wind" : 0,
            "tornado" : 0,
            "tsunami" : 0,
            "volcanic activity" : 0,
            "wildfire" : 0,
            "winter weather" : 0
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

    
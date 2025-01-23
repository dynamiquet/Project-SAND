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
    
import csv, sys

def is_disaster(string):
    valid_disaster_list = ["avalanche", "coastal flooding", "cold wave", "drought", "earthquake", "hail",
                           "heat wave", "hurricane", "ice storm", "landslide", "lightning", "riverine flooding", 
                           "strong wind", "tornado", "tsunami", "volcanic activity", "wildfire", "winter weather"]
    
    if string.lower() not in valid_disaster_list:
        return False
    else:
        return True

def is_us_county(county):

    with open('Data/County_and_Disasters_only.csv', 'r') as file:
        disasterdata = csv.reader(file)
        for row in disasterdata:
            if str(row[0]).lower() == county.lower():
                return True

        return False
    file.close()
    
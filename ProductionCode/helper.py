import csv, sys

def valid_disaster(string):
    valid_disaster_list = ["avalanche", "coastal flooding", "cold wave", "drought", "earthquake", "hail",
                           "heat wave", "hurricane", "ice storm", "landslide", "lightning", "riverine flooding", 
                           "strong wind", "tornado", "tsunami", "volcanic activity", "wildfire", "winter weather"]
    
    return 0

def valid_county(county):

    with open('Data/County_and_Disasters_only.csv', 'r') as file:
        disasterdata = csv.reader(file)
        for row in disasterdata:
            print(row[0])
            if row[0] == county:
                return True
            else:
                return False
    
    file.close()
    
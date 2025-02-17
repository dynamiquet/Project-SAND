## Project S.A.N.D.

### Functionality
This program allows the user to interact with our dataset that contains data about natural disasters in the United States collected by FEMA.

### Using Website (Flask)
In order to use this website concatenate arguments into the browser with ' / ' followed by either: 

Usage One: name of disaster(s) seperated by commas / name of US county, State abbreviation

    Example: 
    (existing url)/Tornado,Earthquake/Los Angeles,CA
This returns the hazard rating for the type of disaster(s) in the given county as recorded by FEMA's dataset

Usage Two: top5/name of US county, State abbreviation

    Example: (existing url)/top5/Rice,MN
This returns the top five most hazardous disaster's in a given county

### Using CLI
You may use the program to obtain National Risk Index data about a particular disaster in a particular county in the U.S. by running the following commands:

Command Line Function 1:
```
python3 command_line.py --disaster 'type_of_disaster(s)' --county 'name_of_US_county, State_abbreviation'
```
Purpose: Returns a hazard rating for each disaster given in the targeted county


Command Line Function 2: 
```
python3 command_line.py --top5 'name_of_US_county, State_abbreviation'
```

Purpose: Returns the top 5 most hazardous disaster's in a given county





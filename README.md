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

## Webpage "Don't Make Me Think" implementations
### Scanability

My page enables scanability by being simple and following standard webpage practices. 

At the top center, the home page title is bolded and has the largest font size of all texts. Below it, is a navigation bar with short and explicit names for what pages they direct you to.

Continuing the top-down scan, huge text describes what a user should search for. The text boxes also have placeholders for the kind of accepted searches.

The available disasters are neatly placed in a box with icons visually describing the kind of disaster.

At the end, a big orange submit button is there catching user attention.

### Satisficing

My web page hopefully encourages no thinking! Given the explicit names of titles, buttons, and input forms a user should be easily able to get what they are searching for. 

### Muddling through

Given the simple layout, users can click and input anything and be directed to proper usage or other resources. 

If they get lost, the first option in the navigation bar is a "Home" page for quick and easy access to the original homepage to start over! If they are otherwise used to clicking the title to go back to the homepage, that is also available! (Currently only for displaying data, but will be integrated to all pages)





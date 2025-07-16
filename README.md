# Project SAND

Project SAND is a dataset-centered web application that allows users to interact in meaningful and useful ways with FEMA's dataset that contains ***up-to-date??*** data about natural disasters in the United States.
comprehensive solution for [brief description of what your project does]. This project aims to [explain the main goal or purpose of your project]. It is built using [mention the main technologies or frameworks used], ensuring high performance and scalability.

## Sample Use Cases
- Feature 1: [Brief description of feature 1]
- Feature 2: [Brief description of feature 2]
- Feature 3: [Brief description of feature 3]

## Features
- Feature 1: [Brief description of feature 1]
- Feature 2: [Brief description of feature 2]
- Feature 3: [Brief description of feature 3]

## Installation
To install and set up the project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/project_SAND.git
    ```
2. Navigate to the project directory:
    ```sh
    cd project_SAND
    ```
3. Install the dependencies:
    ```sh
    npm install
    ```

## Usage
To run the project, use the following command:
```sh
npm start
```
For detailed usage instructions, refer to the [usage documentation](link-to-usage-docs).

## Contributing
We welcome contributions! Please read our [contributing guidelines](link-to-contributing-guidelines) to get started.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any questions or feedback, please reach out to [Your Name] at [your-email@example.com].






## Project S.A.N.D.

## Code Design Improvements
1. Inconsistent function, variable, and class naming style
    - In various locations among our files, there was never a consistent style on naming items. Our helper.py file was the biggest culprit of this.Multiple functions had variables seperated by underscores (example_variable), while others were simply one long word (examplevariable).
    - Specifically, get_string_rating() and get_disaster_risk_dict() had variables called "intratingdict" and "riskvaluelistindex" which should be seperated. These functions found in heplper.py were on lines 38 and 188.
    - To fix inconsistent naming, we combed over files like helper.py to fix inconsistent variable naming conventions and made them clearer in context and seperated by underscores.

2. Bloater: Long Methods
    - Although not in our submitted "front-end" tagged commit, later commits introduced many javascript functions like initmap() which created a unique GoogleMaps map centered on the user's location. The problem with functions like initmap() and many more javascripts functions following it, was that they were too long!
    - To fix this, we split these bloated functions into several smaller one-dimensional functions that did one job well.
    - For example, initmap(), would become a combination of more descriptive functions like getCurrentLocation(), getUserCounty(), setMapInfoWindow(), etc. that are smaller in size and focus on a one-layer abstraction. This map example is found in the javascript file script.js


## Front-End Design Improvements
1. Usability Issue: Unware of Current County Name
    - Our website depended heavily on user knowledge of their current county. To fix this potential issue, we included a "My Current Location" page which grabs the user's coordinates, and disaplys their county name in a GoogleMaps map.
    - This addition was included as an option in our navigation bar present in all pages of our project.
2. Usability Issue: Assumption of Fine motor skills to click all disaster checkboxes
    - Previously, if users wanted to view the disaster risk ratings for all available disasters, they had to click every disaster checkbox to do so. With more than 15 disasters and small checkboxes, the task depended heavily on user motor skills
    - To address the issue, we included a "Check All Disasters!" checkbox to avoid unecessary time effort into checking all available disasters. With one click, all disasters would be checked in the homepage.
    - To avoid having users uncheck all disasters if they changed their minds, we also included the functionality to uncheck all disasters of the "Check All Disasters!" checkbox is unchecked.

---
## Previous CIDER and Functionality Descriptions:

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






# **Team (AJ)^2's User Analysis**

## Contents:

- *CIDER Discussion*
- *Command-Line Benefits*


This file contains the analysis of our command line app’s features’ potential users, as well as their potential benefits and harms/exclusion to the users using the CIDER assumption elicitation technique.


### CIDER Discussion
In coming together to discuss our program's embedded assumption's about the user, the most prominent ones we agreed on are as followed:
1. Our program assume the user is aware of the name of their county or desired area of interest
2. Our program assume the user has knowledge of the recorded disasters in our dataset (Riverine Flooding, Winter Weather, etc.)
3. Our program assumes the user resides in the United States

With these assumptions in mind, we imagined the following scenarios:
1. The user wants to know how dangerous their county is, but they do not know the name of their county. They are upset with our software and potentially feel negatively about themselves.
2. The user knows the name of their county but does not recognize any of the disasters returned. They may be upset with our software for promising information but requires knowledge of the subject matter already.
3. A user from outside the United States wanting information on disasters for their city/province/state would be unable to use our program since the data only contains US counties. 

In hopes to prevent user's from feeling excluded or harmed in any way, we designed the following potential solutions to our program's assumptions:
1. A GUI in the form of the United States divided into its counties would allow users to find their county.
2. Hyperlinks or informational texts (with references to credible sources like FEMA) about the specifc disasters returned.
3. Find data on natural disasters in other countries/continents and create different versions of the program for each respective country/continent depending on how much data is available. EM-DAT has an international natural disaster database that could be used. 

This was our team's analysis of our current command line app’s features’ on potential users using the CIDER assumption elicitation technique

### Command-Line Benefits
The following are some of the benefits we found our program's features to have:
- The program uses precise information by using a really small area (county), instead of using, say state. That allows the user to obtain accurate information.
- The program uses data from a trustworthy source (FEMA), which guarantees users easy access to technical information that is typically difficult to navigate.

# **Team (AJ)^2's User Analysis**

This file contains the continuing analysis of our software as we develop it through multiple sprints.

## Contents:

- *Command Line Interactions Analysis (Sprint 1)*
- *Flask Web App User Analysis (Sprint 2)*
- *Database Sprint*
- *User Analysis and CIDER for the Front-End*  
<br>
<hr>
<br>

## Command Line Interactions Analysis (Sprint 1)
### CIDER Discussion
In coming together to discuss our program's embedded assumption's about the user, the most prominent ones #we agreed on are as followed:
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

<br>

## Flask Web App User Analysis (Sprint 2)

### User Analysis for Flask App Features. 
Overview of this analysis builds upon our previous sprint, where we evaluated the potential users and their experiences with the command-line interface (CLI). Now, we extend our analysis to account for the shift from a CLI to a Flask-based web application, examining the benefits, harms, and exclusion risks posed by the new interaction mechanism.

Potential Users (Carried Over and Expanded):
- Same users from CLI analysis: Users assessing disaster risks, researchers, emergency managers, and general users.
- New user groups introduced by the web interface:
1. Casual users who prefer graphical interfaces over command-line interfaces.
2. Mobile users accessing the data from their phones.
3. Non-technical users who are unfamiliar with command-line inputs but can navigate a website.

- New Embedded Assumptions in Flask-Based Interaction:
1. Users can correctly format their input in the URL structure.
2. Users can navigate a web-based interface comfortably.
3. Users can understand the error messages and follow usage instructions.
4. Users have internet access and a compatible device.

- Potential Harms/Exclusion in Flask Web App:
1. URL-Based Input Restrictions: Users unfamiliar with structured URL inputs may struggle to enter queries correctly.
2. Navigation Challenges: Some users may not easily find the instructions on the homepage.
3. Mobile Accessibility: The interface might not be optimized for mobile users, limiting access.
4. Limited Error Handling: Confusing error messages could frustrate users and discourage engagement.
5. Internet & Device Dependency: Unlike a local CLI, the Flask app requires internet access and a compatible browser, excluding users with limited connectivity.

- Proposed Solutions:
1. Improve User Input Experience:
2. Enhance Navigation & Instructions:
3. Provide a step-by-step guide on the homepage with visual examples.
4. Highlight important instructions at the top of the page.
5. Ensure responsive design for mobile compatibility.
een sizes.

- Improve Error Handling & Messaging:
1. Use user-friendly error messages with clear guidance (e.g., “County not found, try selecting from our list”).
2. Redirect users to a troubleshooting page with common mistakes and solutions.


### Conclusion
The transition from CLI to a Flask-based web application introduces new interaction mechanisms, broadening accessibility but also introducing new usability challenges. By addressing these through improved input handling, navigation, mobile compatibility, and accessibility features, we can enhance the inclusivity and effectiveness of the application. 


#  Database Sprint



###  Assumptions Embedded in Data Collection Methods
1. **Assumption: Data is Comprehensive and Unbiased**
   - The dataset assumes that all counties in the United States are equally represented in the risk assessments.
   - However, some counties may have better data collection mechanisms, leading to overrepresentation or underrepresentation of certain disaster risks.
   - Historical data might be biased toward regions with better reporting infrastructure, potentially skewing the risk values.
   
2. **Assumption: Risk Values Accurately Represent Future Risks**
   - The dataset assumes that historical risk values are a reliable predictor of future disaster occurrences.
   - This does not account for climate change, urban development, or other dynamic factors that could alter risk levels over time.

###  Alternative Data Collection Approaches
1. **Improving Representation:**
   - Instead of relying solely on historical records, the dataset could incorporate real-time climate models and remote sensing data to enhance risk predictions.
   
2. **Accounting for Future Risk Variables:**
   - A model that includes projected climate patterns, urban expansion, and human activity could refine risk predictions.
   - Machine learning techniques could be used to identify correlations between non-traditional data sources (e.g., social media posts during disasters, insurance claims) and actual disaster occurrences.

###  Mitigating Embedded Biases in the Database
1. **Ensuring Geographic Representation:**
   - Implementing data validation checks to identify and address underrepresented regions.
   - Using external databases (e.g. NOAA climate models,...) to cross-check risk values.
  
2. **Handling Missing Data:**
   - Implementing an interpolation model that estimates missing values based on neighboring counties' data.
   - Using uncertainty scoring to flag counties where risk values may be unreliable due to missing or outdated data.

### Conclusion
While the current dataset provides a structured way to assess disaster risks, embedded assumptions about data comprehensiveness and predictive accuracy need to be addressed. Future iterations of the database should incorporate additional data sources and real-time updates to improve reliability. By implementing these strategies, the database can better serve disaster preparedness efforts and provide more accurate insights for risk assessment.

### **User Analysis and CIDER for the Front-End**  

#### **Potential Users**  
The front-end design of Project S.A.N.D. aims to reach a wide audience by making natural disaster data easily accessible. The potential users include:  

1. General Public – Individuals concerned about the disaster risks in their county or state.  
2. Researchers & Environmental Analysts – Those studying the impact of natural disasters on different regions.  
3. Emergency Responders & Government Officials – People involved in disaster preparedness and response planning.  
4. Homeowners & Insurance Companies – Those assessing risks for insurance policies and property investments.  
5. Students & Educators – Those using disaster risk data for academic research and educational purposes.  

#### **Potential Benefits**  
The front-end design improves accessibility and usability compared to the previous command-line and Flask-based interfaces. Key benefits include:  

1. User-Friendly Interface – Unlike command-line interactions, users no longer need to memorize syntax; they can navigate through a structured GUI.  
2. Visual Representation of Data – Icons, color-coded risk levels, and charts improve readability.   
3. Mobile Compatibility – Users can access disaster data on smartphones, making it more convenient.  
4. Improved Error Handling – Clear error messages help users understand mistakes and navigate correctly.  

#### **CIDER Analysis of Embedded Assumptions**  

##### **Assumption 1: Users Can Understand and Navigate the Web Interface**  
-  This assumption does not account for individuals with low digital literacy or those unfamiliar with disaster-related terminology.  
-  A user with minimal technology experience may struggle to interpret the results or navigate through dropdowns and checkboxes.  
- **Design:**  
  - Implement tooltips and hover explanations for disaster-related terms (We have some resources on the resources page).    
  - Ensure tab-based navigation and keyboard shortcuts for accessibility.  

##### **Assumption 2: The Website is Accessible Across All Devices and Internet Speeds**  
-  The site may be optimized for desktops but could face performance issues on mobile devices or slow internet connections.  
-  A user on a low-bandwidth connection or an older mobile device may experience slow load times or broken UI elements.  
- **Design:**  
  - Use responsive design to ensure a seamless experience across different screen sizes.  
  - Optimize images and scripts to reduce load time, especially for mobile users.

#### **Assumption 3: The Website is Accessible to All Users, Including Those with Disabilities**
- Critique:
1. The site assumes that all users can see colors and images clearly, navigate with a mouse, and read small text.
2. Screen reader users might face issues if form elements aren’t labeled properly.
Imagine:
A visually impaired user navigating with a screen reader might struggle if labels are missing.

- **Design Fixes**:
1. Ensure high color contrast for readability.
2. Provide text descriptions for risk levels and have a ressources pages for more informations.


  
### **Conclusion**  
The front-end interface of our Project S.A.N.D. significantly enhances usability and accessibility, making disaster risk data more accessible to a broader audience. However, assumptions about user digital literacy and device compatibility must be addressed to ensure inclusivity. Implementing guided tutorials, optimized design for low-bandwidth users, and accessibility features will improve user experience and make the platform more effective for diverse audiences. 

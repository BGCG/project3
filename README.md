# BloodTracker
 
## Background
 
Blood cells have proteins on the surface of them called antigens. These include A, B as well as D antigens. The presence of these proteins on the cells determine their blood type - A (contains A antigens), B (contains B antigens), AB (contains both A and B) and O (contains no A or B antigens). Additionally, people can also have a D antigen (also known as Rhesus D protein or Rh for short). This means some people are positive or negative for D/Rh.
 
Blood types are typically expressed by the A/B/AB/O followed by whether they have the D protein (Positive or Negative) i.e. APOS. If a patient is transfused with blood from an incompatible blood type, i.e. a person with A blood is transfused with B blood, the patient will have a transfusion reaction due to the recipient patient's immune system attacking the B proteins in the transfused blood.
 
Patients of different blood types have a different immune repertoire which attacks incompatible blood types in the form of antibodies. This incompatibility is summarised below:
 
* Patients with A blood have antibodies to B proteins
* Patients with B blood have antibodies to A proteins
* Patients with O blood have antibodies to both A and B proteins
* Patients with AB blood have no antibodies to A and B proteins
 
Additionally, patients can have the D proteins on their blood cells (POS), while patients who are negative for D proteins will have antibodies against the D proteins so cannot be transfused with D+ blood.
 
Even though there are other proteins on blood cells that can cause an immune reaction; A, B and D proteins are considered highly 'clinically relevant' proteins in transfusion reactions (rch.org, 2023).
 
There are departments and health centers dedicated to testing for blood types and in providing transfusion services, which are often understaffed in the UK due to spending cuts. This can make keeping up with stocks of blood difficult and not surprisingly wastage occurs due to expiration of blood. This highlights the need for computerised tracking software to manage the stocks of blood to ensure a smooth running of blood centers and donation services. The BloodTracker app aims to solve this issue in donation services by providing easy information regarding how many blood units are in store and whether any are expired.
 
![amiresponsive-screenshot](/assets/images/intro_screenshot.jpg)
 
The live site can be found [here](https://blood-tracker-app.herokuapp.com/). This project was created for the purpose of submission to the Code Institute full stack software development diploma program.
 
## UX design
 
### Site purpose
 
Blood donation wastage is a significant problem for transfusion services around the world. One study has reported that 77.9% of discarded blood was wasted due to time expiry (Far et al., 2013).
 
Blood stored at 6<sup>o</sup>C is considered optimal for 35 days (Blood.co.uk, 2023). When blood is in storage, it goes through a series of biological changes called storage lesion, making the donation progressively less effective in transfusion (Oyet et al., 2018). One study has indicated that usage of expired blood can result in increased risk of death (Wang et al., 2014).
 
BloodTracker is a blood stock management system which is intended for use in a healthcare system where doctors and nurses can easily check how many units of blood they have left, as well as which are expiring and need to be discarded.
 
### Current user goals
 
* To check the number of blood donations of a particular blood type is left
* To be easily informed which blood stocks are expired for discarding
* To prevent the accidental usage of expired blood
 
### Repeated user goals
 
* Due to the nature of this app, users will repeat usage of the tool in a manner the same as current user goals would.
 
### Communication
 
The user inputs the blood type they would like to check and they are presented with information regarding the number of units left and expiry.
 
### Audience
 
The site is aimed towards those working in the blood donations and transfusion services such as doctors, nurses and other healthcare workers.
 
### Future goals
 
To integrate with input of donations data so the stocks can be adjusted based on donations coming in and also when a donation is used that will be subtracted. A machine learning algorithm could be useful in order to predict the usage of certain blood types so donor cohorts can be automatically invited to come into donation centers to give blood and replenish stocks. Additionally, to modify the database to include all the clinically relevant blood cell antigens i.e. Kell, Duffy and Kidd system antigens.
 
## Design
 
### Wireframes
 
![flowchart](/assets/images/blood-app-flowchart.jpeg)
 
Chart created using LucidChart premium free trial

## Features
 
### Landing page
 
* Introduction to app
 
![introduction](/assets/images/start.jpg)
 
### User input and validation
 
* User prompted to input what blood type they would like to perform a stock check on
* The user input is checked that it is in the correct format.
 
![input_validation](/assets/images/input_validation.jpg)

* If the input is invalid, the user will be alerted of this. 

![invalid_input](/assets/images/invalid_input.jpg)
 
### User feedback
 
* User is alerted to the number of donations left of a particular blood type - blood donations are grouped based on identifiers
* Additionally, users can see information on units left and expiration dates of blood.
 
![stock_list](/assets/images/stock_list.jpg)
 
### Units
 
* If the units of blood are below 10,000 units, the user will be alerted they are running out of a particular blood type/ID.
 
![stock_low](/assets/images/stock_low.jpg)
 
* If units of blood are above 10,000 then the user will be informed they have enough stock for future transfusions.
 
![sufficient_stock](/assets/images/sufficient_stock.jpg)
 
### Expiration
 
* If the expiration of a blood type sample exceeds today's date - the user will be alerted to this and asked to discard the sample.
 
![stock_exp](/assets/images/stock_exp.jpg)
 
* If all stock of a particular blood type is within expiry, the user will be informed of this.
 
![within_expiry](/assets/images/within_exp.jpg)
 
* Expiration checker is only accurate for the GMT timezone.
 
### Exit or restart
 
* Once the desired information has been provided to the user, the user will be asked whether they would like to check the stock of another blood type or if they would like to exit the program.
 
![restart_or_quit](/assets/images/restart_or_quit.jpg)
 
### Features yet to implement
 
* Stock predictor
* Automated donor cohort alert to replenish stocks
 
## Limitations
 
As there are variations in the number of units of blood used in hospitals per week and times of the year as well as differences in demands in blood types due to genetic differences between populations, it is difficult to determine how many units of blood of a particular type is classed as a 'low amount'. Therefore, 10K units of blood as the low limit cut off point is likely inaccurate. If this project was pursued further I would look at statistical reports to determine which is the best unit cut off point for a particular blood type in a particular population, but to actually predict future blood usage may require machine learning algorithms.
 
## Testing
 
The main areas of testing were ensuring that the user input was validated effectively. I tested the input by putting in the wrong string, similar strings (i.e. `POS`), blank and other characters i.e. `!` to the input to determine how robust the validation was, which always activated the invalid response message. I wrote a conditional statement that detects whether the user has entered a blood type exactly as stated in the options list. I did want to allow some leniency on the users part, such as if there was an accidental space before or after the input word, as this couldn't be misunderstood as a different input for which I used the `strip()` method. Additionally, it doesn't matter whether the user used upper, lower or captilised input as this would not change the interpretation of the user input. I converted all the user inputs to uppercase using the `upper()` method. Not converting the user input to uppercase would result in the invalid input message showing, as I found when I forgot to include it in the testing process. Furthermore, I didn't allow white space mid word in options, i.e. `A B POS` as this might be misinterpreted by the program as BPOS when in fact the user wanted results for ABPOS. In addition to my own testing, my mentor and tutor support also tested the app deployed on Heroku for incorrect input and found that the app did not crash.
 
With regards to the validate input function, I did have some issues that the rest of the script would still activate even if the invalid response was activated and would not surprisingly report `None` and empty lists for stock level reports. I therefore fixed my conditional statement in the validate input function so that the while loop would only be exited if the user input was in the options lists, by using boolean logic.
 
An additional area of testing was whether correct values are reported to the user. For the stock list report, I formed a dictionary to store values in the program and iterated through the dictionary to find whether there were instances that matched the user's input and fed this back to the user. I tested by inserting every blood type and double checking the values against the google sheets, for which I did not find any inconsistencies.
 
## Bugs
 
* To my knowledge, bugs that have been detected have been fixed. I have elaborated on bugs experienced during development of this app in the testing section of this README.
 
## Validators
 
* Passing the python code for this app through the PEP8 validator produced no errors.
 
![PEP8-validator-results](/assets/images/validator_results.jpg)
 
## Credits
 
### Content
 
Love sandwiches Code Institute project for the help with initial set up and wire up of the API for which I had no clue how to do this before walking through the tutorial.
 
I have used list comprehension throughout this project. The following resource from [W3 Schools](https://www.w3schools.com/python/python_lists_comprehension.asp) was a useful reminder on how to perform list comprehensions.
 
I was a little nervous about using date time in my program as I heard that they are notoriously difficult to work with in programming. A little reading online and usage of the datetime library was helpful. This [stack overflow](https://stackoverflow.com/questions/36424255/python-iterating-through-a-list-using-datetime-strptime) post was particularly helpful in figuring out how to convert the expiry dates from the google sheets into a more workable format. I converted the expiry dates and today's date into isocalendar format which forms into a tuple object which was then used for comparison between each other.
 
Creation of dictionaries from two lists - I found the reply from Martijn Pieters on this [stack overflow](https://stackoverflow.com/questions/72076666/create-a-dictionary-from-multiple-lists-one-list-as-key-other-as-value) post very helpful in me figuring this out. Furthermore, when providing feedback to the user I wanted to provide the dictionary in a neat tabular format for which I installed the tabulate library. This [resource](https://www.educba.com/python-print-table/) was helpful in figuring out how to use the tabulate module.
 
To remove square brackets when alerting users which blood batch ID was low or expired, I found the reply from Vicent on [stack overflow](https://stackoverflow.com/questions/13207697/how-to-remove-square-brackets-from-list-in-python) who suggested converting the list to a string followed by `[1:-1]` in the print statement.
 
### Main language used
 
* Python
 
### Libraries and frameworks used
 
* GitPod - the developer platform was used as a space to code the app which was then pushed to Github
* GitHub - to store the app prior to connecting Heroku
* [Heroku](https://www.heroku.com) - for deployment to live terminal
* [LucidChart](https://www.lucidchart.com/) - for wireframing, which an image of the wireframe created in LucidChart is provided in the Design section of this README
* [AmIResponsive](https://ui.dev/amiresponsive) - for the screenshot of how the app will look across different devices, which is included in the introduction to this README
* [citethisforme.com](citethisforme.com) - to generate website references
 
#### Python libraries
 
* gspread - for working with google sheets in this Python project
* datetime - to easily manipulate the date and time object
* google-auth - to provide authentication to the API
* tabulate - to easily produce neat tables for user feedback
 
### Deployment
 
* Ensure new lines are inserted in input statements to ensure compatibility with Heroku
* Create requirements file by entering `pip3 freeze > requirements.txt` into terminal and commit and push changes
* Go to heroku.com and go to dashboard and `create new app`
* New app was named `blood-tracker-app`
* Select region where you are working
* Go to settings tab and create config vars - `KEY:CREDS VALUE:` (all contents of creds.json), `KEY:PORT VALUE:8000`
* Add buildpacks - `heroku/python` and `heroku/nodejs` - in that order
* Go to deploy tab and connect to GitHub
* Find project in `BGCG` by searching `project3` and selecting connect
* Deploy branch to main by manual deploy
* Click `Deploy Branch` - once this is completed you will see a `View` button which you can click to open you application
 
 
### Dataset
 
* I created a mock dataset that would represent a real world dataset for the purpose of this project. Though I appreciate the mock dataset is a simplified version of the real world data which would likely report other information such as different proteins on the blood cells surface and have individual identifiers for each blood type (I grouped these based on blood type and their expiration, but within that group their could be different patients giving that blood).
 
#### Dataset column headers explanations
 
* Blood type: blood type of batch expressed as ABO type followed by Rh status i.e. APOS.
* Units: number of units of blood within that batch.
* Expiration: expiration date of blood batch. The idea being that the whole batch was collected by different patients on a particular day and then 35 days from there is the expiry.
* Blood batch ID: the ID of that full blood batch (different numbers assigned based on when the blood was collected of a particular type).
 
### People
 
* My mentor for her valuable feedback and Code Institute tutor support.
 
## References for information in README introduction  
 
Blood cell antigens and blood incompatibility are common knowledge in the field of medical biology so no reference is required for those particular facts.
 
### References for specific studies and information in websites:
 
* Far RM, Rad FS, Abdolazimi Z, Kohan MM. Determination of rate and causes of wastage of blood and blood products in Iranian hospitals. Turk J Haematol. 2014 Jun;31(2):161-7.
 
* How your donation gets to the patient. NHS Blood Donation. Available at: https://www.blood.co.uk/news-and-campaigns/the-donor-magazine-autumn-2017/how-your-donation-gets-to-the-patient/#:~:text=All%20test%20results%20are%20recorded,kept%20for%20only%20five%20days (Accessed: January 11, 2023).
 
* Oyet C, Okongo B, Onyuthi RA, Muwanguzi E. Biochemical changes in stored donor units: implications on the efficacy of blood transfusion. J Blood Med. 2018 Jun 25;9:111-115.
 
* The Royal Children's Hospital Melbourne. Available at: https://www.rch.org.au/bloodtrans/about_blood_products/Blood_Groups_and_Compatibilities/ (Accessed: January 11, 2023).
 
* Wang D, Sun J, Solomon SB, Klein HG, Natanson C. Transfusion of older stored blood and risk of death: a meta-analysis. Transfusion. 2012 Jun;52(6):1184-95.
 
 
 
 
 


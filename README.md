# BloodTracker

## Background 

Blood cells have proteins on the surface of them called antigens. These include A, B as wells a D antigens. 

The presence of these proteins on the cells determine their blood type - A (contains A antigens), B (contains B antigens), A/B (contains both A and B) and O contains no antigens. 

Additionally, people can also have a D antigen (also known a Rhesus D protein or Rh for short). This means some people are positive or negative for D/Rh.

Blood types are typically expressed by the A/B/O followed by whether they have the D protein (Positive or Negative) ie APOS.

If a patient is transfused with blood from an incompatible blood type ie a A person is transfused with B blood, the patient will have a transfusion reaction due to the recipient patients immune system attacking the B proteins in the transfused blood. 

Patients of different blood types have a different immune repitore which attacks incomaptible blood types in the form of antibodies. This incomaptibility is summarised below:

* Patients with A blood have anti-bodies to B proteins 
* Patients with B blood have anti-bodies to A proteins
* Patients with O blood have antibodies to A and B proteins 
* Patients with AB blood have no antibodies to A and B proteins 

Additionally, patients can have the D proteins on their blood cells (POS), while patients who are negative for D proteins will have antibodies against the D proteins so cannot be transfused with D+ blood. 

Even though their are other proteins on blood cells that can cause an immune reaction; A, B and D proteins are considered the most likely to elicit an immune reactions and are often described as the most 'clinically relevant' proteins in transfusion reactions. 

There are departments and health centers dedicated to testing for blood types and in providing transfusions services, which are often understaffed in the UK due to spending cuts. This can make keeping up with stocks of blood difficult and no surprising wastage occurs due to expiration of blood. 

This highlights the need for computerised tracking software to manage the stocks of blood to ensure a smooth running of blood centers and donation services.

The BloodTracker app aims to solve this issue in donation services by providing easy information regarding how many blood units are in store and whether any are expired.

![amiresponsive-screenshot](/assets/images/intro_screenshot.jpg)

The live site can be found [here](https://blood-tracker-app.herokuapp.com/). This project is still under development and was created for the purpose of submission to the Code Institute full stack software deploma program.

## UX design

### Site purpose 

Blood donation wastage is a significant problem for transfusion services around the world. One study has reported that 77.9% of blood was wasted due to time expiry (Far et al., 2013).

Blood stored at 6<sup>o</sup>C is consider optimal for 35 days, after which a process called hemolysis generally occurs where blood cells start bursting, making the donation not recommeded for use. One study has indicated that usage of expired blood can result in increased risk of death (Wang et al., 2014). 

BloodTracker is a blood management system which is intended for use in a healthcare system where doctor and nurses can easliy check how many units of blood they have left, as well as which are expiring and need to be discarded.

### Current user goals 

* To check the number of blood donations of a particular blood type is left
* To be easily informed which blood stocks are expired for discarding 
* To prevent the accidental usage of expired blood

### Repeated user gaols

* Due to the nature of this app, users will repeat usage of the tool in a manner the same as current user goals would. 

### Communication

The user inputs the blood type they would like to check and they are presented with informations regarding the number of units left and expiry. 

### Audience 

The site is aimed towards those working in the blood donations and transfusion services such as docotors, nurses and other healthcare workers. 

### Future goals 

To integrate with input of donations data so the stocks can be adjusted based on donations coming in and also when a donation is used that will be subtracted. A machine learning algorithm could be useful in order to predict the usage of certain blood types so donor cohorts can be automatically invited to come in to donation centres to give blood and replenish stocks. 

## Design 

### Wireframes 

![flowchart](/assets/images/blood-app-flowchart.jpeg)

Chart created using Lucid Chart premium free trial

## Features

### Landing page 

* Introduction to app 

![introduction](/assets/images/start.jpg)

### User input and validation

* User prompted to input what blood type they would like to perform a stock check on
* The user input is checked that it is in the correct format.

![input_validation](/assets/images/input_validation.jpg)

### User feedback

* User is alerted to the number of donations left of a particular blood type - blood donations are grouped based on identifiers
* Additionally, users can see information on units left and expiration dates of blood. 

![stock_list](/assets/images/stock_list.jpg)

### Units

* If the units of blood are below 10,000 units, the user will alerted we are running out of a particular blood type/id

![stock_low](/assets/images/stock_low.jpg)

* If units of blood are above 10 then the user will be informed they have enough stock for future donations. 

![sufficient_stock](/assets/images/sufficient_stock.jpg)

### Expiration

* If the expiration of a blood type sample exceeds todays date - the user will be alerted to this and asked to discard the sample 

![stock_exp](/assets/images/stock_exp.jpg)

* If all stock of a particular blood type is within expiry, the user will be informed of this.

![within_expiry](/assets/images/within_exp.jpg)

* Expiration is only accurate for GMT timezone 

### Exit or restart

* Once the desired information has been provided to the user, the user will be asked whether they would like to check the stock of another blood type or if they would like to exit the program. 

![restart_or_quit](/assets/images/restart_or_quit.jpg)

### Features yet to implement

* Stock predictor 
* Automated donor cohort alert to replenish stocks

## Limitations

As there are variations in the number of units of blood used in hospitals per week and seasons (i.e. late summer due to increased car crashes) as well as differences in demands in blood types due to genetic differences between populations, it is difficult to determine how many units of blood of a particular type is classed as a 'low amount'. Therefore, 10K units of blood cap is likely unaccurate. If this project was persued further I would look at statistical reports to determine which is the best unit cut of point for a particular blood type, but to actually predict future blood usage may require machine learning algorithms.

## Testing 

The main areas of testing where ensuring that the user input was validated effectively. I tested the input by puting in the wrong string or similar strings (ie POS) to the input to determine how robust the validation was, which always activated the invalid response. I wrote a conditional statement that detects whether the user has entered an blood type exactly as stated in the options list. I did want to allow some leaniancy on the users part, such as if there was an accidental space before or after the input word, as this couldn't be misunderstood as a different input for which I used the `strip()` method. Additionally, it doesn't matter whether the user used upper, lower or captilised input as this would not change the interpretation of the user input. I converted all a user inputs to uppercase using the `upper()` method. Not converting the user input to uppercase would result the invalid input message showing, as I found when I forgot to include it in the testing process. Furthermore, I didn't allow white space mid word in options, ie 'A B POS' as this might be misinterpretted by the program as BPOS when in fact the user wanted results for ABPOS. 

With regards to the validate input function, I did have some issues that the rest of the script would still activate even if the invalid response was activated and would not surprisingly report None and empty lists for stock level reports. I therefore fixed my conditional statement in the validate input function so that the while loop would only be exited if the user input was in the options lists, by using of boolean logic. 

An additional area of testing was whether correct values are reported to user. I formed a dictionary to store values in the program and iterated through the dictionary to find whether there were instances that matched the users input and fed this back to the user. I tested by inserted every blood type and double checking the values against the google sheets, for which I did not find any inconsistencies. 

## Bugs 

* To my knowledge, bugs that have been detected have been fixed. I have elaborated on bugs experienced during development of this app in the testing section of this README. 

## Validators 

* Passing the python code for this app through the PEP8 validator produced no errors. 

![PEP8-validator-results](/assets/images/validator_results.jpg)

## Credits 

### Content 

Love sandwiches Code Institute project for the help with intial set up and wire up of the API for which I had no clue how to do this before walking through the tutorial. 

I have used list comprehension throughout this project. The following resource from [W3 Schools](https://www.w3schools.com/python/python_lists_comprehension.asp) was a useful reminder on how to perform list comprehensions.

I was a little nervous about using date time in my program as I heard that they are notoriously difficult to work with in programming. A little reading online and usage of the datetime library was helpful. This [stack overflow](https://stackoverflow.com/questions/36424255/python-iterating-through-a-list-using-datetime-strptime) post was partiuclarly helpful in figuring out how to convert the expiry dates from the google sheets into a more workable format. I converted the date into isocalendar format which forms into a tuple object which was then used for comparision with todays date, converted into the sample iscalendar format.

Creation of dictionarys from two lists - I found the reply from Matryn Peters on this [stack overflow](https://stackoverflow.com/questions/72076666/create-a-dictionary-from-multiple-lists-one-list-as-key-other-as-value) post very helpful in me figuring this out. Furthermroe, when providing feedback to the user I wanted to provide the dictionary in a neat tabular format for which I installed the tabulate library. This [resource](https://www.educba.com/python-print-table/) was helpful in figuring out how to use the tabulate module.

### Libraries and frameworks used

* GitPod - the developer platform was used as a space to code my site which was then pushed to Github
* GitHub - to store the app prior to connecting Heroku
* Heroku - for deployment to live terminal
* Lucid Chart - for wireframing, which an image of the wireframe created in Lucid Chart is provided in the Design section of this README
* AmIResponsive - for the screenshot of how the app will look across different devices, which is included in the introductio to this README

### Deployment 

* Ensure new lines are inserted in input statements to ensure compatibility with Heroku
* Create requirements file by entering pip3 freeze > requirements.txt into terminal and commit and push changes 
* Go to heroku.com and go to dashboard and create new app 
* New app was named blood-tracker-app
* Go to settings tab and create config vars - KEY:CREDS VALUE:(all contents of creds.json), KEY:PORT VALUE:8000
* Add buildpacks - heroku/python and heroku/nodejs - in that order
* Go to deploy tab and connect to GitHub 
* Find project in BGCG by searching 'project3' and selecting connect 
* Deploy branch to main in manual deploy


### Dataset 

* I created a mock dataset that would represent a real world dataset for the purpose of this project. Though I appreciate the mock dataset is a simpflified version of the real world data which would likely report other information such as different proteins on the blood cells surface and have individual identifiers for each blood type (I grouped these based on blood type and their expiration, but within that group their could be different patients giving that blood).

### People

* My mentor for her valuable feedback.

## References for information in README introduction  

* Far RM, Rad FS, Abdolazimi Z, Kohan MM. Determination of rate and causes of wastage of blood and blood products in Iranian hospitals. Turk J Haematol. 2014 Jun;31(2):161-7. 

* Wang D, Sun J, Solomon SB, Klein HG, Natanson C. Transfusion of older stored blood and risk of death: a meta-analysis. Transfusion. 2012 Jun;52(6):1184-95. 



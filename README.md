# BloodTracker

## Background 

Blood cells have proteins on the surface of them called antigens. These include A, B as wells a D antigens. 

The presence of these proteins on the cells determine their blood type - A (contains A antigens), B (contains B antigens), A/B (contains both A and B) and O contains no antigens. 

Additionally, people can also have a D antigen (also known a Rhesus D protein or Rh for short). This means some people are positive or negative for D/Rh.

Blood types are typically expressed by the A/B/O followed by whether they express the D proteins (Positive or Negative) ie APOS.

If a patient is transfused with blood from an incompatible blood type ie a A person is transfused with B blood, the patient will have a transfusion reaction due to the patients immune system attached the B proteins in the transfused blood. 

Patients of different blood types have a different immune repitore which attacks incomaptible blood types in the form of antibodies. This incomaptibility is summarised below:

* Patients with A blood have anti-bodies to B proteins 
* Patients with B blood have anti-bodies to A proteins
* Patients with O blood have antibodies to A and B proteins 
* Patients with AB blood have no antibodies to A and B proteins 

Additionally, patients can have the D proteins on their blood cells (POS), while patients who are negative for D proteins will have antibodies against the D proteins so cannot be transfused with D+ blood. 

Even though their are other proteins on blood cells that can cause an immune reaction; A, B and D proteins are considered the most likely to elicit an immune reactions and are often described as the most 'clinically relevant' proteins in transfusion reactions. 

There are departments and health centers dedicated to testing for blood types and in performing transfusions services which are often understaffed in the UK due to spending cuts. This can make keeping up with stocks of blood difficult and no surprising wastage occurs due to expiration of blood. 

This highlights the need for most computerised tracking software to manage the stocks of blood to ensure a smooth running of blood centers and donation services. 

## UX design

### Site purpose 

Blood donation wastage is a significant problem for transfusion services around the world. One study has reported that 77.9% of blood was wasted due to time expiry (Far et al., 2013).

Blood stored at 6<sup>o</sup>C is consider optimal for 14 days, after which a process called hemolysis generally occurs where blood cells start bursting, making the donation not recommeded for use. One study has indicated that usage of expired blood can result in increased risk of death (Wang et al., 2014). 

BloodTracker is a blood management system which is intended for use in a healthcare system where doctor and nurses can easliy check how many units of blood they have left and which are expiring and need to be discarded. 

### Current user goals 
* To check the number of blood donations of a particular blood type is left
* To be easily informed which are expired for discarding 
* To use as a tool to alert donor cohorts to replenish stocks on the basis they are easily told clearly when a blood type is running out 
* To prevent the accidental usage of expired blood

### Repeated user gaols
* Due to the nature of this app, users will repeat usage of the tool in a manner the same as current user goals would. 

### Communication

The user inputs the blood type they would like to check and they are presented with informations regarding the number of units left and expiry. 

### Audience 

The site is aimed towards those working in the blood donations and transfusion services such as docotors, nurses and other healthcare workers. 

### Future goals

To integrate with input of donations data so the stocks can be adjusted based on donations coming in and also when a donation is used that will be subtracted. A machine learning algorithm could be useful in order to predict the usage of certain blood types so donor cohorts can be automatically invited to come in to donation centres to give blood and replenish stocks. 

## Features

### Landing page 
* Introduction to app 

### User input
* User prompted to input what blood type they would like to perform a stock check on

### User feedback 
* User is alerted to the number of donations left of a particular blood type - blood donations are grouped based on identifiers
* Additionally, users can see information on units left and expiration dates of blood. 

### Units 
* If the units of blood are below 10 units, the user will alerted we are running out of a particular blood type/id

### Expiration 
* If the expiration of a blood type sample exceeds todays date - the user will be alerted to this and asked to discard the sample 
* Expiration is only accurate for GMT timezone 

### Exit or restart
* Once the desired information has been provided to the user, the user will be asked whether they would like to check the stock of another blood type or if they would like to exit the program. 

### Features yet to implement 
* Stock predictor 
* Automated donor cohort alert to replenish stocks

## Testing 

Testing correct user input 

Testing whether correct values are reported to user 

## Validators 

* PEP8 (insert screenshot) 

## Credits 

### Content 

Love sandwiches for the intial set up and wire up of the API for which I had no clue how to do this before walking through the tutorial. 

List comprehesion - I have used list comprehension throughout this project. The following resources were useful reminders how to perform list comprehension - 

Datetime - I was a little nervous about using date time in my program as I heard that they are notoriously difficult to work with in programming. A little reading online and usage of the datetime library was helpful. I converted the date into isocalendar format which forms into a tuple object. This was then used for comparision with todays date, converted into the sample iscalendar format.

Creation of dictionarys from two lists - i found this resource helpful in me figuring this out. 

### Libraries and frameworks used 
* GitPod
* GitHub
* Heroku 

### Deployment 

- go through it step-by-step

### Dataset  
* I created a mock dataset that would represent a real world dataset for the purpose of this project. Though I appreciate the mock dataset is a simpflified version of the real-world data which would likely report other information such as different proteins on the blood cells surface and have individual identifiers for each blood type (I grouped these based on blood type and their expiration, but within that group their could be different patients giving that blood).

### People
* My mentor for her valuable feedback.

## References for information in README introduction  
* Far RM, Rad FS, Abdolazimi Z, Kohan MM. Determination of rate and causes of wastage of blood and blood products in Iranian hospitals. Turk J Haematol. 2014 Jun;31(2):161-7. 

* Wang D, Sun J, Solomon SB, Klein HG, Natanson C. Transfusion of older stored blood and risk of death: a meta-analysis. Transfusion. 2012 Jun;52(6):1184-95. 



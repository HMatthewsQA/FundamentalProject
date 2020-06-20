# Corona Patient Testing DB

## My Resources:
* Trello: https://trello.com/b/lDIlmUeF/corona-virus-db

## Contents
* [Brief](#brief)
   * [Additional Requirements](#additional-requirements)
   * [My Approach](#my-approach)
* [Architecture](#architecture)
   * [Database Structure](#database-structure)
   * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Authors](#authors)

## Brief

To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

### Additional requirements

* Trello board for project tracking
* A relational database
* Clear documentation
* Application created in python
* Testing
* Functioning front end
* Use version control system

### My approach

The application I have chosen to create is a corona virus testing database and application. This will constist of four tables: Facilities, Patients, Doctors and Tests. The relationships of these shall be laid out in another section. A user will be able to create and read records from any of the four tables, as well as update patients in the database and delete test records. To help me measure my progress whilst developing this project I have made use of a trello board to track my progress. I have also made use of git and github as a version control system for project development. The application itself has been developed using elements of python, html and sql to create a funcioning system. Testing has been implemented using pytest in order to assure that the application is running as intended and that errors are avoided.

## Architecture

### Database Structure

I have created an entity relationship diagram, or ERD, to help illustrate the relationships taking place in my database that operates behind the scenes of my application. 


![ERD][erd]


The database makes use of one to many relationships as well as primary and foreign keys to assign facilities, patients and doctors to a test that has been performed and added.

### CI pipeline

I have created an image to show the process of my continous integration pipeline.


![CI][ci]




## Project Tracking

Below is a screenshot from my trello board towards the end of the development process.


![Trello][trello]


Here I have tracked user stories and tasks for completion so that development runs smoothly and to prevent tasks being forgotten or objectives being missed.

## Risk Assessment


![RiskAssessment][riskassessment]


I have completed a risk assessment to help me understand the ways that my application and its resources might come under threat and how I can plan to mitigate or prevent these circumstances.

## Testing

I have carried out a number of tests on my project, the results of these can be found in my test results folder. I have included both unit and integration tests.


![Coverage][coverage]


I have achieved 80% coverage in my testing. This is because while I have tested all of my models and forms, I have not yet implemented tests for all of the routes that make up my application.

## Known Issues

There are currently some issues in the application and database with elements of data that are supposed to be unique as I have not yet implemented validation into the record creation process. This means that if a user tries to create a record with data that is already in use in a field that is supposed to be unique it will cause an error.

## Future Improvements

For future improvements of my project I would like to implement a better design for the user interface of the application. This will make it more user friendly and make performing interactions easier. Additionally I would like to add more tests so that I can achieve a better coverage to ensure that all aspects of the application and database are being tested and performing well. Furthermore I would like to implement more validation into the application to prevent avoidable errors from being thrown up when a user tries to input data.

## Authors

Harry Matthews

[erd]: https://github.com/HMatthewsQA/FundamentalProject/blob/master/Documents/ProjectERD.png?raw=true "Database ERD"
[riskassessment]: https://github.com/HMatthewsQA/FundamentalProject/blob/master/Documents/RiskAssessment.png?raw=true "Risk Assessment"
[trello]: https://github.com/HMatthewsQA/FundamentalProject/blob/master/Documents/Trello%20Dev/Trello4.png?raw=true "Trello Board"
[ci]: https://github.com/HMatthewsQA/FundamentalProject/blob/master/Documents/CIPipeline.png?raw=true "CI Pipeline"
[coverage]: https://github.com/HMatthewsQA/FundamentalProject/blob/master/Documents/coverage.png?raw=true "coverage"
# imdb_pytest_gui
***
Test automation of IMDB Top Rated Movies page.

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)

### General Info
***
Automation of few functionalities in IMDB top rate movies page is done.
Data-driven Framework using Page Object Model design pattern and selenium.
Python is the language used for scripting.

Mutliple Browser execution, parallel execution, execution across various operating systems and HTLM reporting supported.

***
Automated Test Scenarios:
1. Test scenario: Verify the movie chart has 250 movies in it and Sort by functionality
2. Test Scenario: Verify Search in IMDB web page and navigate back to home page
3. Test Scenario: Verify Wish list before and after user signed in

## Technologies
***
A list of technologies used within the project:
* Python: Version 3.9.0
* pip: Version 21.0.1
* PyCharm (Community Edition):Version  2020.3.3
* pytest: Version 6.2.2
* xlrd: Version 1.2.0
* pytest-xdist: Version 2.2.1
* pytest-html: Version 2.4.7
* webdriver manager
* Selenium

## Installation
***
For the project to run properly in any environment follow the below steps
```
Precondition: Pyton Version 3.9.0 and pip: Version 21.0.1 should be pre installed

Steps:
1. Clone and extact project from git path: https://github.com/deepthi-mohan/imdb_pytest_gui
2. Open project in Pycharm
3. In Pycharm terminal run following commands:

   $ pip install -U selenium (To install selenium)
   $ pip install pytest (to install pytest)       
   $ pip install pytest-xdist (to enable parallel execution)
   $ pip install webdriver-manager  (to install web driver manager) 
   $ pip install pytest-html  (to enable html reporting)
   $ pip install xlrd==1.2.0 (to read data from excel)

4. To run the imdb_pytest_gui project 
   
   To run and generate html report use command: $ pytest -v -s --html=<name of report to be generated> eg:$ pytest -v -s --html=test_report.html
   To run and see details in console run command :$ pytest -v -s
   To as parallel execution: $py.test -n <enter number of browsers needed> eg:$py.test -n 5
   To run in parallel and generate report :$pytest -n <enter number of browsers needed> -v -s --html=<name of report to be generated>
                                          eg: $pytest -n 5 -v -s --html=test_report.html
   
Note: To select browsers edit imdb_pytest_gui\config\\config.py file fixture.
      By default chrome is selected

 





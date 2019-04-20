Homeworks and class assignments from NYU Advance Python course May - August 2018
Professor: David Blaikie 

S = Sessions hw = Homework cl = in-class 

Session 1 -- Parsing Tabular Data; Objects, Types, Functions, Containers (ETL) 
  
    Program reads weather data for New York from data obtained from the Weather Underground website (this is provided in           the session_1_working_files in the source data folder), then computes the count of values collected, max and min               temps, average (mean) temp, and standard deviation from the daily mean column.
  Submitted file: s1hw.py
        
Session 2 -- Data Aggregation and Primary Keys; Multidimensional Containers and Sorting
    
    Sum volume by buyer (i.e., total volume for each buyer), then join the aggregated result with ad_companies to show the         name of each buyer.  Include only active buyers that appear in the ad_companies table.
    Gereate these in a tuple via built-in python, sql and pandas.
  Submitted file: s2hw.py
  
Session 3 -- Functions, Modules, Packages, Testing

    Write the "wrapper" module, which provides a simplified interface to a few of the date functions of the the standard           distribution datetime module. The module should also be capable of raising a TypeError or ValueError exception with a         customized message if the user of the module calls the module's functions incorrectly.
  Submitted file: date_simple.py, __init__.py, test_date_simple.py, s3hw.py

Session 4 -- Classes, HTML
    
    A custom-designed Stock object that is populated with data from a data source (the web or database) and is "inserted" into     a display HTML page.
  Submitted: s4hw.py, ticker.html
  
Session 5 -- Data Model, Attribute Access and Templating

    Create a product catalog database. Next create a script that when ran takes 2 arguments (id and state) and product details     and image are populated into HTML and loaded on a webpage. 
  Submitted: s5hw_ETL.py, s5hw.py
  
Session 6 -- Web Programming, Flask

    Flask application based on Stock data from session 5. 
  Submitted: ticker.py, product_flask.py

    

# Data Analytics Migration Tableau

## Project Brief 
Clean and present 10 years of flight data for your company. Using PostGreSQL on AWS RDS to store the cleaned and transformed data in order to enable a data analysis, 
Integrate Tableau with the PostGreSQL RDS to visually explore the data and to create visulaistaions and various real-time charts using the back-end flights data stored in RDS.
Prepare a presentation to share with top management highlighting the insights and findings observed.

## Project dependancies 
In order to run this project the following need to be installed and/or imported:
- json
- requests
- os
- bs4
- selenium
- time


## Connecting to the local database using pgAdmin
pgAdmin is used to connect to the local database. With pgAdmin installed and running, follow these steps to connect:

1. On the main application page, click on 'Add New Server'
![image](https://github.com/Mat-Zawadzki/data-analytics-migration-to-tableau/assets/114954374/06f2a958-9ffa-44b5-866e-cbb2961752c9)

2. On the 'General' tab of the dialogue that appears, enter a name for the new server connection
![image](https://github.com/Mat-Zawadzki/data-analytics-migration-to-tableau/assets/114954374/741d2bf6-0e7a-4f15-857b-eeb1bcb2e380)

3. On the 'Connection' tab, enter 'localhost' for the 'Host name/address', and enter the username and password specified when creating the database.

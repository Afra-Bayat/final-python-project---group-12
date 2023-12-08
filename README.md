# DAB 111 - Python Final Project

### Group Members:

Group No. 12

- Adyan Ahmad Quazi - 0852399
- Boontarika Ubonyaen - 0836724
- Masoumeh Bayat - 0809145
 
 
### Project Objective:

This project contains the usage of Python, Pandas, SQLite3, and Flask. Using Pandas, we are reading data from dataset and stored in database using SQLite3 package. Flask is used to present stored data of database on web.
Website contains mainly 3 pages, Home, About, and Dataset. About Us page shows the details about each variable definition. Dataset page shows the number of immigrants from the specified country in each respective year from 1980 to 2013. 



### Overview

This project revolves around acquiring Canadian immigration data from Kaggle, integrating this data into an SQLite database using the sqlite3 package in Python, and subsequently visualizing these records within a table. Utilizing Python's SQLite integration for data storage, Flask for web development, HTML for content structure, CSS for styling, and the Kaggle dataset on Canadian immigration, this project aims to create an interactive website that showcases and allows exploration of the immigration data in a user-friendly manner.


### Source of Data

The dataset is sourced from Kaggle and is named "Immigration to Canada"

*Link to Source:* [Source link](https://www.kaggle.com/datasets/ammaraahmad/immigration-to-canada)


## Example Usage
 ### Download required modules first:

 - Run command "pip install -r requirements.txt"
 - This will install all required packages for this project

 ### Run app Locally:

Step 1:
-Clone the project first or download zip of project and extract it

 (you can access the 'canadian_immegration_data.csv' in Database folder)

 Step 2:
 - If you not see 'immigration.db' file in Database directory, then open new terminal in 'database' folder
 - Run "creating-db.py" command, this will create new database file, create a table and insert data from 'canadian_immegration_data.csv' file

Step 3:
 - Open 'terminal' or 'cmd' in root directory of the project
 - Run "python app.py" command
 - Go to http://127.0.0.1:5000
 - And explore the website
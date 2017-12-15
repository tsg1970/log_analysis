Udacity Python Log Analysis Project

Python Log Analysis

website: https://github.com/tsg1970/log_analysis.git
email: tsgoff@att.net

# Project Overview

To create reporting tool that prints out reports based on the data in a
PostGresql database. The reporting tool is a Python program using the psycopg2
module to connect to the database.

The database can be downloaded at the following link: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
Unzip the file into the same directory as a virtual machine.

The file used to access the database is newsdatadb.py. Save file in the same directory
as the database. To access the reporting tool type newsdatadb.py at a command prompt.

The code answers 3 questions:
  What are the most popular three articles of all time?
  Who are the most popular article authors of all time?
  On which days did more than 1% of requests lead to errors?

Data Science Salary Estimator  U.K: Project Overview

Salary of position based on the other factors associated with the job are varies. So created a tool that estimates data science salaries  to help data scientists negotiate their income when they get a job In U.K.



Data Collection

I used glassdoor web scraper and Scraped over 1000 job descriptions from glassdoor using python and selenium
Data Description
Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
 job postings from glassdoor.com. With each job, we got the following:
Job title
Salary Estimate
Job Description
Rating
Company
Location
Company Headquarters
Company Size
Company Founded Date
Type of Ownership
Industry
Sector
Revenue
Competitors

Data Cleaning

After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:
Parsed numeric data out of salary
Made columns for employer provided salary and hourly wages
Removed rows without salary
Parsed rating out of company text
Made a new column for company state
Added a column for if the job was at the company’s headquarters
Transformed founded date into age of company
Made columns for if different skills were listed in the job description:
Python
R
Excel
AWS
Spark
Column for simplified job title and Seniority
Column for description length

EDA

I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 
Data-science jobs in different sectors

![download (1)](https://user-images.githubusercontent.com/32133030/127942656-29044333-e3af-434b-8579-e995d6d7273b.png)
![download (2)](https://user-images.githubusercontent.com/32133030/127942743-7830281d-33df-4100-bc27-608f62e0e0df.png)
![download (4)](https://user-images.githubusercontent.com/32133030/127942756-0a591c43-ae4f-4c8a-9cd9-c32e94a123f8.png)

Model Building/Engineering

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.
I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.
I tried three different models:
Multiple Linear Regression – Baseline for the model
Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.

Model performance

The Random Forest model far outperformed the other approaches on the test and validation sets.
Random Forest : MAE = 11.22
Linear Regression: MAE = 18.86
Ridge Regression: MAE = 19.67


Product-ionization

In this step, I built a flask API endpoint that was hosted on a local web-server by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 

Code and Resources Used

Python Version: 3.7
Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
For Web Framework Requirements: pip install -r requirements.txt

Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:24:42 2020

@author: vinay
"""

import pandas as pd

df = pd.read_csv('out 2.csv')

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K', '').replace('£', ''))
df[ 'min_salary'] = minus_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary' ] = minus_kd.apply(lambda x: int(x.split('-')[1]))
df['average_salalry'] = (df.min_salary + df.max_salary)/2
df['comapny_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else  x['Company Name'][:-3], axis =1)
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[0])
df['age'] = df['Founded'].apply(lambda x: x if x < 1 else 2020 - x)
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R_yn'] =  df['Job Description'].apply(lambda x:1 if 'r studio' in x.lower() else 0)
df.R_yn.value_counts()
df['spark'] =  df['Job Description'].apply(lambda x:1 if 'spark' in x.lower() else 0)
df.spark.value_counts()
df['aws'] =  df['Job Description'].apply(lambda x:1 if 'aws' in x.lower() else 0)
df.aws.value_counts()
df['excel'] =  df['Job Description'].apply(lambda x:1 if 'excel' in x.lower() else 0)
df.excel.value_counts()
df.columns
df.to_csv('salary_data_cleaned.csv', index = False)

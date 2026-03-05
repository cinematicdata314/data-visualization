# Data Visualization Projects

This repository contains several data analysis and visualization projects implemented in **Python using Pandas, Matplotlib, Seaborn, and GeoPandas**.  
The projects explore real-world datasets including fuel price trends, geographic volcano data, and COVID-19 statistics.

The goal of these projects is to demonstrate **data cleaning, exploratory data analysis, time series analysis, and data visualization techniques** using Python.

---


# Project 1: Ontario Fuel Price Analysis

## Overview
This project analyzes weekly retail fuel prices across multiple Ontario cities using data from the **Ontario Fuel Price Survey dataset**. The analysis focuses on comparing fuel prices between cities and examining the distribution of gasoline prices.

## Dataset
Ontario Government Fuel Price Survey  
https://data.ontario.ca/dataset/fuels-price-survey-information

## Tools Used
- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  



## 1. Average Fuel Prices by City (2022)

A **bar chart** compares the mean price of Regular Unleaded Gasoline across Ontario cities during 2022.

Steps:
- Filter dataset for *Regular Unleaded Gasoline*
- Select data from the year **2022**
- Compute the **mean price per city**
- Visualize the results using a bar chart

This visualization highlights **regional price differences across Ontario markets**.



## 2. Distribution of Gasoline Prices in Ottawa

A **histogram** visualizes the distribution of Regular Unleaded Gasoline prices in Ottawa during 2022.

This analysis helps identify:

- Price variability  
- Most common price ranges  
- Overall spread of fuel prices  



## 3. ECDF of Gasoline Prices

An **Empirical Cumulative Distribution Function (ECDF)** plot shows the cumulative probability distribution of gasoline prices in Ottawa during 2022.

This visualization helps determine the **probability that gasoline prices fall below a given value**.

---

# Project 2: Time Series and Geospatial Analysis

This project expands the fuel dataset analysis and introduces **time series analysis and geospatial visualization**.

## Tools Used

- Python  
- Pandas  
- Matplotlib  
- GeoPandas  



## 1. Fuel Price Time Series (London, Ontario)

### Dataset
https://data.ontario.ca/dataset/fuels-price-survey-information

### Objective
Analyze long-term gasoline price trends.

### Method

- Filter dataset for **Regular Unleaded Gasoline**
- Select data between **2000 and 2022**
- Convert date column to datetime format
- Apply a **5-week Simple Moving Average** to smooth fluctuations

### Visualization

A **time series line chart** displays smoothed gasoline prices over time.  
This helps reveal **long-term pricing trends and market fluctuations**.



## 2. Volcano Location Map

### Dataset
Volcano Database  
https://github.com/plotly/datasets/blob/master/volcano_db.csv

### Objective
Visualize volcano locations in **North America**.

### Method

- Filter volcano data for:
  - Canada
  - United States
  - Mexico
- Convert latitude and longitude coordinates into geospatial points
- Plot volcano locations using **GeoPandas**

### Visualization

A geographic map showing **volcano locations across North America**.

This demonstrates **geospatial data processing and mapping techniques in Python**.

---

# Project 3: COVID-19 Impact Analysis

## Overview

This project analyzes the relationship between **COVID-19 vaccination rollout and pandemic outcomes** using publicly available datasets.

The analysis focuses on three key indicators:

- COVID-19 cases  
- Hospitalizations  
- Deaths  

## Datasets

COVID-19 Case Data  
https://open.canada.ca/data/en/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6

COVID-19 Death Data  
https://data.ontario.ca/en/dataset/deaths-involving-covid-19-by-fatality-type

COVID-19 Hospitalization Data  
https://data.ontario.ca/en/dataset/covid-19-cases-in-hospital-and-icu-by-ontario-health-region

## Tools Used

- Python  
- Pandas  
- Matplotlib  



## 1. COVID-19 Cases by Year

A **bar chart** aggregates total COVID-19 cases by year using Ontario public health data.

This visualization highlights how the pandemic evolved over time.



## 2. Hospitalizations and ICU Patients

A **monthly time series chart** compares:

- COVID-19 hospitalizations  
- ICU patients  

This visualization shows how severe COVID-19 cases fluctuated over different phases of the pandemic.



## 3. COVID-19 Death Trends

A **time series plot** tracks deaths caused by COVID-19 over time.

This analysis highlights periods of increased mortality during different waves of the pandemic.



## 4. Death Classification Analysis

A multi-line chart compares different categories of COVID-19 related deaths:

- Total deaths involving COVID-19  
- COVID-19 as underlying cause  
- COVID-19 as contributing cause  
- Unknown causes  






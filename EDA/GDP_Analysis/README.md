# GDP Analysis Project

## Overview
This project explores global GDP data for 56 countries spanning from 1960 to 2018. The goal is to gain an in-depth understanding of economic performance by analyzing GDP growth trends, comparing GDP across countries, and visualizing data using interactive graphs. GDP (Gross Domestic Product) is a key measure of a country's economic performance as it represents the total value of all goods and services produced over a specified period.

## Project Structure & Steps

### 1. GDP Analysis - Assignment
- **Objective:** Work with a dataset containing GDP data for 56 countries and answer a series of quiz questions related to GDP growth.
- **Tasks:** 
  - Load the dataset.
  - Analyze the data to answer questions about GDP growth.
  - Submit answers based on your analysis.

### 2. Dataset Walkthrough
- **Objective:** Familiarize yourself with the dataset and identify any potential issues or limitations.
- **Task:** 
  - Display the initial rows of the dataset using `df.head()` to get a quick overview of the data structure.

### 3. GDP Growth of a Country
- **Objective:** Calculate the annual GDP growth rate for a specific country.
- **Task:** 
  - Identify GDP values for consecutive years.
  - Use the formula:  
    `GDP growth rate = ((GDP_current - GDP_previous) / GDP_previous) * 100`  
    to calculate the percentage change.
  - Add the calculated growth as a new column in the dataset.
  - Verify the results with manual calculations.

### 4. GDP Growth on the Whole Dataset
- **Objective:** Extend the GDP growth calculation across all countries in the dataset.
- **Task:** 
  - Loop through each country to compute the annual GDP growth.
  - Handle missing data appropriately (filling or skipping as needed).
  - Concatenate the new GDP growth values back to the original dataset.
  - Verify the output to ensure accuracy.

### 5. Plotting Graphs Using Plotly
- **Objective:** Enhance data visualization with interactive and dynamic graphs.
- **Tasks:** 
  - Install and import Plotly libraries (`plotly.express` and `plotly.offline`).
  - Create line graphs to visualize global GDP trends and specific country data (e.g., India).
  - Add titles, labels, and interactive elements.
  - Save graphs as HTML files for offline viewing.

### 6. Plotting Graphs in Bulk
- **Objective:** Automate the generation of interactive GDP graphs for all countries.
- **Tasks:** 
  - Use a loop to iterate through each country in the dataset.
  - Generate and save individual HTML graphs for each country.
  - Organize the output by creating a dedicated directory for the graphs.

### 7. Compare GDP across Countries
- **Objective:** Visualize and compare the GDP growth of two or more countries.
- **Tasks:** 
  - Filter the dataset to include only the countries you want to compare.
  - Use Plotly to create interactive line graphs with clear labeling and color differentiation.
  - Save the comparative graph as an HTML file.

### 8. Compare GDP Growth Comparison (Advanced)
- **Objective:** Automate and refine the process of comparing GDP growth among multiple countries.
- **Tasks:** 
  - Import necessary libraries and set up the environment.
  - Handle missing data and remove outliers to ensure robust comparisons.
  - Loop through each country to generate dynamic visualizations for GDP growth over time.
  - Save each interactive graph with a descriptive filename.

## Installation & Requirements
- **Python:** Version 3.6 or later
- **Libraries:** 
  - pandas
  - plotly
  - os (standard library)
- **Setup:** Install the required libraries using pip:
  ```bash
  pip install pandas plotly

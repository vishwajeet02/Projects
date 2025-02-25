# Sugarcane Production Analysis

Welcome to the Sugarcane Production Analysis project! This repository houses a Jupyter Notebook that dives into sugarcane production data from around the world. Using Python and powerful libraries like Pandas, Seaborn, and Matplotlib, this analysis uncovers trends, relationships, and insights from the dataset "List of Countries by Sugarcane Production.csv."

## Table of Contents

- [Sugarcane Production Analysis](#sugarcane-production-analysis)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Setup](#setup)
  - [Dataset](#dataset)
  - [Analysis Breakdown](#analysis-breakdown)
    - [Data Cleaning](#data-cleaning)
    - [Univariate Analysis](#univariate-analysis)
    - [Bivariate Analysis](#bivariate-analysis)
    - [Correlation Analysis](#correlation-analysis)
    - [Analysis by Continent](#analysis-by-continent)
  - [Key Insights](#key-insights)

## Project Overview

This project explores sugarcane production across countries and continents, analyzing key metrics like total production, yield efficiency, and land usage. Whether you're a data enthusiast, researcher, or just curious about global agriculture, this notebook provides a clear, visual, and data-driven journey through the numbers behind sugarcane.

## Setup

To run the notebook, ensure you have the following Python libraries installed:

pip install pandas seaborn matplotlib

- Pandas: For data manipulation and aggregation.
- Seaborn: For beautiful, statistical visualizations.
- Matplotlib: For customizable plotting.

Clone this repository and open the Jupyter Notebook in your preferred environment (e.g., JupyterLab, VS Code, or Jupyter Notebook).

## Dataset

The dataset, "List of Countries by Sugarcane Production.csv," includes sugarcane production details for various countries. It features the following columns:

| Column                     | Description                                           |
|----------------------------|-------------------------------------------------------|
| Country                    | Name of the country                                   |
| Continent                  | Continent where the country is located                |
| Production (Tons)          | Total sugarcane production (in tons)                  |
| Production per Person (Kg) | Production per capita (in kilograms)                  |
| Acreage (Hectare)          | Land area used for sugarcane (in hectares)            |
| Yield (Kg / Hectare)       | Production efficiency per hectare (in kilograms)      |

## Analysis Breakdown

### Data Cleaning
- Steps: Removed unwanted characters (e.g., commas, dots) from numeric columns for consistency; dropped irrelevant columns.
- Notes: Minor future warnings during cleaning were noted but don’t impact the analysis.

### Univariate Analysis
- Focus: Examines individual variables (e.g., production, yield).
- Visuals: Bar plots and distribution plots highlight data spread and outliers.

### Bivariate Analysis
- Focus: Explores pairwise relationships, like land area vs. production or yield vs. production.
- Visuals: Scatterplots and bar plots reveal trends and dependencies.

### Correlation Analysis
- Focus: Measures how numeric variables relate (e.g., production and acreage).
- Visuals: A heatmap displays the correlation matrix, spotlighting strong or weak links.

### Analysis by Continent
- Focus: Aggregates data by continent to compare production, yield, and land use.
- Visuals: Bar and line plots showcase continental differences.

## Key Insights

This analysis reveals:
- Which countries dominate sugarcane production and why.
- How production correlates with land area and yield efficiency.
- Continental patterns in sugarcane cultivation.
- Unexpected trends, like outliers in per-capita production.

For a deeper dive, explore the Jupyter Notebook!

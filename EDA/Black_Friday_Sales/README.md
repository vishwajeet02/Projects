# Black Friday Sales Data Analysis

## Overview
Black Friday is a major shopping event held the day after Thanksgiving, famous for its significant discounts and deals across various product categories like electronics, home goods, and clothing. This project analyzes the Black Friday Sales dataset to identify purchasing patterns and insights based on user demographics such as age, gender, occupation, and marital status.

The dataset contains detailed information about Black Friday shoppers and their purchases, enabling us to explore trends and behaviors through data analysis and visualization.

---

## Prerequisites
To follow along with this project, you need:
- **Basic Python**: Knowledge of Python programming fundamentals.
- **Pandas**: Familiarity with data manipulation and analysis using Pandas.
- **Matplotlib & Seaborn**: Understanding of these libraries for creating visualizations (e.g., bar plots, count plots).
- **Jupyter Notebook**: Ability to run Python code interactively in a Jupyter environment.
- **Basic Data Analysis**: Skills in data cleaning, handling missing values, and performing exploratory data analysis (EDA).

---

## Dataset Details
- **Name**: Black Friday Sales Data
- **Size**: 23 MB CSV file, with over 537,000 rows and 12 columns.
- **Columns**:
  - `User_ID`: Unique identifier for each user.
  - `Product_ID`: Unique identifier for each product.
  - `Gender`: Gender of the customer (M/F).
  - `Age`: Age group of the customer (e.g., 0-17, 18-25).
  - `Occupation`: Occupation code of the customer.
  - `City_Category`: Category of the city (A, B, C).
  - `Stay_In_Current_City_Years`: Duration of stay in the current city.
  - `Marital_Status`: Marital status of the customer (0 for unmarried, 1 for married).
  - `Product_Category_1`: Primary product category.
  - `Product_Category_2`: Secondary product category (contains NaN values).
  - `Product_Category_3`: Tertiary product category (contains NaN values).
  - `Purchase`: Purchase amount in dollars.

---

## Project Steps

### 1. Walkthrough of the Dataset
- **Goal**: Load and inspect the dataset to understand its structure and contents.
- **Actions**:
  - Loaded the dataset into a Pandas DataFrame using `pd.read_csv("BlackFriday.csv")`.
  - Inspected structure with `df.head()`, `df.shape` (537,577 rows, 12 columns), and `df.dtypes`.
  - Checked for missing values using `df.isnull().sum()` (significant NaNs in `Product_Category_2` and `Product_Category_3`).
  - Used `df.info()` for a summary of column types and non-null counts.

### 2. Handling Missing Data
- **Observation**: `Product_Category_2` has 166,986 NaNs, and `Product_Category_3` has 373,299 NaNs out of 537,577 rows.
- **Options**:
  - Dropping all rows with NaNs using `df.dropna()` reduces the dataset to 164,278 rows (~69% data loss).
  - Alternative: Fill NaNs or focus on non-sparse columns for analysis.

### 3. Analyzing Columns
- **Goal**: Explore distributions and relevance of key columns.
- **Actions**:
  - Focused on `Gender`, `Age`, `Marital_Status`, `Product_Category_1`, and `Purchase`.
  - Examined unique values and counts using `unique()` and `nunique()` (not explicitly shown but implied).
  - Noted significant NaN presence in `Product_Category_2` and `Product_Category_3`, suggesting a focus on `Product_Category_1`.

### 4. Analyzing Gender
- **Goal**: Investigate gender distribution and purchasing trends.
- **Actions**:
  - Observed data imbalance: More male customers than female.
  - Planned to use `groupby()` to analyze purchase amounts by gender (not fully implemented in provided code).

### 5. Analyzing Age & Marital Status
- **Goal**: Study how age groups and marital status influence purchases.
- **Actions**:
  - Categorized users by `Age` and `Marital_Status` to identify spending patterns.
  - Planned visualizations (not fully implemented in provided code).

### 6. Multi-Column Analysis
- **Goal**: Combine factors like `Age`, `Gender`, and `Marital_Status` for deeper insights.
- **Actions**:
  - Planned to use visualizations (e.g., pie charts, bar plots) to explore combined effects.

### 7. Occupation and Products Analysis
- **Goal**: Examine how `Occupation` relates to `Product_Category_1` purchases.
- **Actions**:
  - Analyzed relationships between occupation and product preferences (not fully implemented).

### 8. Combining Gender & Marital Status
- **Goal**: Visualize the combined impact of `Gender` and `Marital_Status` on purchases.
- **Actions**:
  - Used `sns.countplot(x='City_Category', hue='Gender_Martial')` (Note: `Gender_Martial` seems to be a typo or undefined column; likely intended as a combination of `Gender` and `Marital_Status`).
  - Plotted count distribution across `City_Category` (not the intended gender-marital combo).

---

## Conclusion
This project aims to uncover Black Friday shopping behaviors by analyzing demographic factors like gender, age, marital status, and occupation. The provided notebook demonstrates initial steps: loading data, checking structure, and handling missing values. While some analysis steps (e.g., gender, age, multi-column) are planned but not fully coded, the final visualization attempts to combine factors, though it currently uses `City_Category` instead of the intended `Gender` and `Marital_Status`.

Future work could include:
- Correcting the `Gender_Martial` typo and implementing the intended analysis.
- Completing groupby operations and visualizations for all planned steps.
- Deciding on a strategy for NaN values (e.g., imputation vs. exclusion).

---

## Requirements
To run the notebook:
```bash
pip install pandas seaborn matplotlib jupyter
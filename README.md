# A/B Testing Analysis with Python and Power BI

![image](https://github.com/user-attachments/assets/da75cd8c-d5ba-4a55-a990-9d83e56a5638)


This repository contains a project that analyzes A/B test results using Python and Power BI. The analysis evaluates whether there are statistically significant differences between two levels (Gate 30 and Gate 40) of a mobile game based on player retention rates and gaming behavior.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Data Analysis Process](#data-analysis-process)
- [Statistical Tests](#statistical-tests)
- [Power BI Dashboard](#power-bi-dashboard)
- [Findings](#findings)
- [How to Use](#how-to-use)
- [Dependencies](#dependencies)

## Project Overview

The goal of this project is to determine whether changes in the game's level design (Gate 30 vs. Gate 40) affect user retention rates and player activity. Statistical analyses and visualizations were performed in Python, while dashboards and interactive reports were created using Power BI.

## Features
- **Statistical Analysis:** 
  - Conducted normality tests and non-parametric tests for retention rates and game rounds.
  - Evaluated whether the differences between the two groups were statistically significant.
  
- **Visualizations:**
  - Used histograms and scatter plots for normality assessment.
  - Created detailed dashboards in Power BI to visualize retention rates and game rounds.

- **Power BI Insights:**
  - Transformed data using Power BI's "Transform Data" feature.
  - Created new measurements using DAX functions.
  - Designed intuitive dashboards for easy interpretation of results.

## Data Analysis Process

### 1. Data Cleaning and Preprocessing
- Removed outliers in the dataset by setting a maximum threshold for game rounds.
- Converted boolean retention values into numerical values for easier analysis.
- Exported cleaned data to Excel for compatibility with Power BI.

> **Note:** Exporting data to Excel is preferred for Power BI users working in Turkish settings. This avoids comma-related issues during data import.

### 2. Statistical Tests in Python
- Performed Z-tests for retention rate comparisons.
- Conducted non-parametric Mann-Whitney U tests for game rounds.
- Verified normality with Shapiro-Wilk tests and visualized distributions using histograms.

### 3. Dashboard in Power BI
- Imported Excel data into Power BI.
- Used the "Transform Data" feature for additional preprocessing.
- Created new **Measurements** using DAX functions for in-depth analysis.
- Designed visualizations such as bar charts, line graphs, and KPIs.

## Statistical Tests

- **Retention 1:** No significant differences were observed between Gate 30 and Gate 40 in terms of Day 1 retention rates.
- **Retention 7:** Conversion rate for Retention 7 was found to be 1. This indicates no significant differences between the two gates.
- **Game Rounds:** Similar game round behavior was observed for both groups, with no significant differences.

### Conclusion
There is no statistically significant difference between Gate 30 and Gate 40 for retention rates and game rounds. The observed differences are likely due to chance.

## Power BI Dashboard

The Power BI dashboard includes:
- Interactive visualizations for comparing retention rates.
- Filters to focus on specific groups or metrics.
- Key performance indicators (KPIs) for quick insights.

## Findings

- There are no meaningful differences between Gate 30 and Gate 40 in terms of player retention or game activity.
- Both levels perform similarly, and any differences are likely coincidental.



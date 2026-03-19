

# Data Drift Detection
https://rizal-data-drift-detection-evidently.streamlit.app/

This repository provides a comprehensive framework for detecting data drift in machine learning pipelines. Data drift occurs when the statistical properties of the input data change over time, potentially leading to model performance degradation.

---

## Overview

In production environments, machine learning models often face **concept drift** or **data drift**. This project focuses on identifying when the distribution of incoming inference data significantly deviates from the training data distribution. By monitoring these shifts, you can trigger retraining processes or investigate data quality issues before they impact your business metrics.

## Key Features

*   **Statistical Tests:** Implementation of various methods like Kolmogorov-Smirnov (K-S) test, Population Stability Index (PSI), and Jensen-Shannon Divergence.
*   **Visualizations:** Tools to plot distribution comparisons between reference (train) and current (production) datasets.
*   **Automated Alerts:** Logic to flag features that exceed defined drift thresholds.
*   **Scalable Design:** Capable of handling both numerical and categorical data features.


## How It Works
1) Reference Baseline: The tool establishes a statistical baseline using a "Reference Dataset" (usually the training set).

2) Feature Profiling: For each feature, the tool calculates statistical properties.

3) Comparison: It compares the current data window against the baseline using the selected statistical test.

4) Drift Scoring: A drift score is generated. If the score exceeds the threshold, the feature is marked as "drifted."
---

## Installation
### Clone the repository:
git clone https://github.com/dreameshuggah/data_drift_detection.git
cd data_drift_detection

### Install the required dependencies:
pip install -r requirements.txt

### Run App
streamlit run streamlit_data_drift.py

# Data Drift Detection

This repository provides a comprehensive framework for detecting data drift in machine learning pipelines. Data drift occurs when the statistical properties of the input data change over time, potentially leading to model performance degradation.

---

## Overview

In production environments, machine learning models often face **concept drift** or **data drift**. This project focuses on identifying when the distribution of incoming inference data significantly deviates from the training data distribution. By monitoring these shifts, you can trigger retraining processes or investigate data quality issues before they impact your business metrics.

## Key Features

*   **Statistical Tests:** Implementation of various methods like Kolmogorov-Smirnov (K-S) test, Population Stability Index (PSI), and Jensen-Shannon Divergence.
*   **Visualizations:** Tools to plot distribution comparisons between reference (train) and current (production) datasets.
*   **Automated Alerts:** Logic to flag features that exceed defined drift thresholds.
*   **Scalable Design:** Capable of handling both numerical and categorical data features.

---



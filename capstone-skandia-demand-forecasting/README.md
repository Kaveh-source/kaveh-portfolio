# Capstone – Product Demand Forecasting (Skandia Elevator)

This folder contains **my main contribution** to a six-person Business Analytics capstone
project with Skandia Elevator (grain handling equipment manufacturer).

The full capstone included three analytics tracks:

1. Product Demand Forecasting  
2. Customer Segmentation & Churn Modeling  
3. Quote Conversion Prediction  

This repository focuses on **Track 1 – Product Demand Forecasting**, which I led.

---

## My Role

- Led the **Product Demand Forecasting** track.
- Aggregated historical order data (2013–2025) to monthly demand for each product category.
- Mapped internal product codes (e.g., `PROVIS`, `RÖR`, `BULT`) to business-friendly
  categories (Provisions, Pipes, Bolts, etc.).
- Built **Holt–Winters (Exponential Smoothing)** models to forecast 12 months of demand
  for the top product categories by volume.
- Created forecast visualizations and helped write the interpretation and recommendations
  in the final capstone report.

Other teammates led the segmentation/churn and quote conversion tracks; their code is
not included here.

---

## Data

- `Cleaned.CustomerOrderRows.csv` – order-level dataset with dates, part IDs,
  delivered quantities, etc.
- `Cleaned.Parts.csv` – part master data with internal codes.

These files are expected to live in the same folder as the script.  
(If the real data is confidential, you can replace it with a smaller synthetic sample.)

---

## Methods & Tools

- **Language:** Python  
- **Libraries:** `pandas`, `matplotlib`, `statsmodels` (`ExponentialSmoothing`)  
- **Approach:**
  - Monthly aggregation of delivered quantity by product category
  - Identification of top 3 categories by total historical volume
  - Holt–Winters modeling for each category (additive trend)
  - 12-month ahead forecasts and visualizations
  - Export of forecast table for use in dashboards or Excel

---

## How to Run

1. Place the following files in this folder:
   - `Cleaned.CustomerOrderRows.csv`
   - `Cleaned.Parts.csv`

2. Run the script:

   ```bash
   python demand_forecasting_kaveh.py


3. Outputs:
   - `figures/`  
     - `<Category>_12_month_forecast.png` for each top category  
     - `combined_12_month_forecast.png`
   - `top_categories_12_month_forecast.csv` – table of 12-month forecasts.

---

## Key Results (from the capstone)

- Identified the top product categories (e.g., Pipes, Bolts, Provisions) by historical demand.
- Forecasted a **rise in pipe demand** over the next year and a **decline in bolts demand**,
  with provisions showing low but volatile demand.
- Provided recommendations for **inventory and production planning** aligned with these
  patterns.

> This work is part of the Skandia Elevator Business Analytics Capstone  
> (Northeastern University, Spring 2025). The code here reflects my individual  
> contribution to the project.


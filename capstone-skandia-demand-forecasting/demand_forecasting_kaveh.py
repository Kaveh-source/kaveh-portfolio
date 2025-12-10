"""
Capstone – Product Demand Forecasting (Skandia Elevator)
Author: Kaveh Jalilian

This script forecasts monthly demand for the top product categories
using Holt–Winters (Exponential Smoothing) on historical order data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from pathlib import Path

plt.style.use("default")

# ===================== 1. LOAD DATA =====================

DATA_DIR = Path(".")  # adjust if your CSVs live elsewhere

orders = pd.read_csv(DATA_DIR / "Cleaned.CustomerOrderRows.csv")
parts = pd.read_csv(DATA_DIR / "Cleaned.Parts.csv")

# ===================== 2. CLEAN & MERGE =====================

orders["OrderDate"] = pd.to_datetime(orders["OrderDate"], errors="coerce")
orders = orders.dropna(subset=["OrderDate"])

orders["DeliveredQuantity"] = pd.to_numeric(
    orders["DeliveredQuantity"], errors="coerce"
).fillna(0)

parts = parts[["PartId", "Code"]].copy()

merged = orders.merge(parts, on="PartId", how="left")

# ===================== 3. MAP TO PRODUCT CATEGORIES =====================

category_mapping = {
    "PROVIS": "Provisions",
    "RÖR": "Pipes",
    "BULT": "Bolts",
    "REM": "Screws",
    "FRAKT": "Delivery Cost",
}

merged["Category"] = merged["Code"].map(category_mapping).fillna(merged["Code"])

# ===================== 4. BUILD MONTHLY DEMAND TABLE =====================

monthly = (
    merged.groupby(
        [pd.Grouper(key="OrderDate", freq="M"), "Category"]
    )["DeliveredQuantity"]
    .sum()
    .reset_index()
)

pivot = (
    monthly.pivot(index="OrderDate", columns="Category", values="DeliveredQuantity")
    .fillna(0)
)

# Drop non-product categories if needed
drop_categories = ["Delivery Cost"]
pivot = pivot.drop(columns=[c for c in drop_categories if c in pivot.columns], errors="ignore")

# ===================== 5. SELECT TOP N CATEGORIES =====================

TOP_N = 3
top_categories = (
    pivot.sum()
    .sort_values(ascending=False)
    .head(TOP_N)
    .index.tolist()
)

print("Top categories by total volume:", top_categories)

# ===================== 6. HOLT–WINTERS FORECAST FUNCTION =====================

def fit_holt_winters(series: pd.Series, periods: int = 12):
    """
    Fit additive Holt–Winters model and forecast 'periods' months.
    - Drops leading all-zero months to stabilize the model.
    - Floors negative forecasts at 0.
    """
    ts = series.asfreq("M")

    non_zero = ts[ts > 0]
    if not non_zero.empty:
        ts = ts.loc[non_zero.index[0]:]

    model = ExponentialSmoothing(ts, trend="add", seasonal=None)
    fitted = model.fit(optimized=True)

    forecast = fitted.forecast(periods)
    forecast[forecast < 0] = 0

    return ts, forecast


# ===================== 7. RUN FORECASTS FOR TOP CATEGORIES =====================

forecast_results = {}

for cat in top_categories:
    history, forecast = fit_holt_winters(pivot[cat])
    forecast_results[cat] = {"history": history, "forecast": forecast}

# ===================== 8. PLOT INDIVIDUAL FORECASTS =====================

FIG_DIR = Path("figures")
FIG_DIR.mkdir(exist_ok=True)

for cat, result in forecast_results.items():
    hist = result["history"]
    fc = result["forecast"]

    plt.figure(figsize=(10, 5))
    plt.plot(hist.index, hist.values, marker="o", label="Historical")
    plt.plot(fc.index, fc.values, marker="o", linestyle="--", label="Forecast")
    plt.title(f"{cat} – 12-Month Demand Forecast")
    plt.xlabel("Month")
    plt.ylabel("Delivered Quantity")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.grid(True, axis="y", alpha=0.3)
    plt.savefig(FIG_DIR / f"{cat}_12_month_forecast.png")
    plt.show()

# ===================== 9. COMBINED FORECAST PLOT =====================

combined_fc = pd.DataFrame(
    {cat: result["forecast"] for cat, result in forecast_results.items()}
)
combined_fc.index.name = "Month"

plt.figure(figsize=(10, 5))
for cat in combined_fc.columns:
    plt.plot(combined_fc.index, combined_fc[cat], marker="o", label=cat)

plt.title("12-Month Forecast – Top Product Categories")
plt.xlabel("Month")
plt.ylabel("Delivered Quantity")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(FIG_DIR / "combined_12_month_forecast.png")
plt.show()

# ===================== 10. EXPORT FORECAST TABLE =====================

combined_fc.to_csv("top_categories_12_month_forecast.csv")
print("Saved 12-month forecast table to 'top_categories_12_month_forecast.csv'")

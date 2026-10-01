import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# --------------------------------------------------
# STEP 1: Connect to MySQL
# --------------------------------------------------

engine = create_engine(
    "mysql+pymysql://root:ashesh2708@localhost/supply_chain_db"
)

# --------------------------------------------------
# STEP 2: Load Sales Data
# --------------------------------------------------

query = """
SELECT
    sale_date,
    quantity_sold
FROM sales
"""

sales = pd.read_sql(query, engine)

# --------------------------------------------------
# STEP 3: Convert Date Column
# --------------------------------------------------

sales["sale_date"] = pd.to_datetime(sales["sale_date"])

# --------------------------------------------------
# STEP 4: Create Monthly Demand Dataset
# --------------------------------------------------

monthly_sales = (
    sales.groupby(
        pd.Grouper(
            key="sale_date",
            freq="ME"
        )
    )["quantity_sold"]
    .sum()
    .reset_index()
)

print("\nMonthly Demand:")
print(monthly_sales.head())

# --------------------------------------------------
# STEP 5: Create Time Index
# --------------------------------------------------

monthly_sales["month_index"] = np.arange(
    len(monthly_sales)
)

# --------------------------------------------------
# STEP 6: Prepare Data
# --------------------------------------------------

X = monthly_sales[["month_index"]]

y = monthly_sales["quantity_sold"]

# --------------------------------------------------
# STEP 7: Train Model
# --------------------------------------------------

model = LinearRegression()

model.fit(X, y)

# --------------------------------------------------
# STEP 8: Predict Existing Values
# --------------------------------------------------

predictions = model.predict(X)

# --------------------------------------------------
# STEP 9: Evaluate Model
# --------------------------------------------------

r2 = r2_score(y, predictions)

print("\nModel Accuracy")
print("R2 Score =", round(r2, 4))

# --------------------------------------------------
# STEP 10: Predict Next Month
# --------------------------------------------------

next_month = [[len(monthly_sales)]]

next_month_prediction = model.predict(
    next_month
)

print(
    "\nPredicted Demand Next Month =",
    round(next_month_prediction[0])
)

# --------------------------------------------------
# STEP 11: Forecast Next 12 Months
# --------------------------------------------------

future_months = pd.DataFrame({
    "month_index": range(
        len(monthly_sales),
        len(monthly_sales) + 12
    )
})

future_months["forecast"] = model.predict(
    future_months
)

print("\n12 Month Forecast")
print(future_months)

# --------------------------------------------------
# STEP 12: Historical Trend Chart
# --------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales["sale_date"],
    monthly_sales["quantity_sold"],
    marker="o"
)

plt.title("Monthly Demand Trend")
plt.xlabel("Month")
plt.ylabel("Quantity Sold")
plt.grid(True)

plt.tight_layout()

plt.show()

# --------------------------------------------------
# STEP 13: Forecast Chart
# --------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales["month_index"],
    monthly_sales["quantity_sold"],
    label="Historical Demand",
    marker="o"
)

plt.plot(
    future_months["month_index"],
    future_months["forecast"],
    linestyle="--",
    marker="o",
    color="red",
    label="Forecast Demand"
)

plt.title("Demand Forecast for Next 12 Months")
plt.xlabel("Month Index")
plt.ylabel("Quantity Sold")
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.show()
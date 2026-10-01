import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# -----------------------------------------
# Connect to MySQL
# -----------------------------------------

engine = create_engine(
    "mysql+pymysql://root:ashesh2708@localhost/supply_chain_db"
)

# -----------------------------------------
# Load Supplier Data
# -----------------------------------------

query = """
SELECT
    supplier_id,
    supplier_name,
    lead_time_days,
    order_frequency
FROM suppliers
"""

suppliers = pd.read_sql(query, engine)

# -----------------------------------------
# Convert Order Frequency to Numeric
# -----------------------------------------

encoder = LabelEncoder()

suppliers["order_frequency_encoded"] = (
    encoder.fit_transform(
        suppliers["order_frequency"]
    )
)

# -----------------------------------------
# Features for Clustering
# -----------------------------------------

X = suppliers[
    [
        "lead_time_days",
        "order_frequency_encoded"
    ]
]

# -----------------------------------------
# K-Means Clustering
# -----------------------------------------

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

suppliers["cluster"] = kmeans.fit_predict(X)

# -----------------------------------------
# Display Results
# -----------------------------------------

print("\nSupplier Clusters\n")

print(
    suppliers[
        [
            "supplier_id",
            "supplier_name",
            "lead_time_days",
            "order_frequency",
            "cluster"
        ]
    ]
)

# -----------------------------------------
# Save Results
# -----------------------------------------

suppliers.to_csv(
    "supplier_clusters.csv",
    index=False
)

print(
    "\nResults saved as supplier_clusters.csv"
)

# -----------------------------------------
# Visualization
# -----------------------------------------

plt.figure(figsize=(10,6))

plt.scatter(
    suppliers["lead_time_days"],
    suppliers["order_frequency_encoded"],
    c=suppliers["cluster"],
    cmap="viridis",
    s=100
)

plt.xlabel("Lead Time (Days)")
plt.ylabel("Order Frequency (Encoded)")
plt.title("Supplier Clustering using K-Means")

plt.colorbar(label="Cluster")

plt.grid(True)

plt.show()
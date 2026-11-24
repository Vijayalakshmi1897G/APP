import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ==========================================
# 1. CREATE SYNTHETIC CHURN DATA
# ==========================================
# Setting a seed for reproducible random generation
np.random.seed(42)
n_samples = 1000

data = {
    "CustomerID": [f"CUST-{i:04d}" for i in range(1, n_samples + 1)],
    "Tenure": np.random.randint(1, 72, size=n_samples),
    "MonthlyCharges": np.random.uniform(20.0, 120.0, size=n_samples),
    # Creating an imperfect TotalCharges string columns with missing blanks to mock real raw data
    "TotalCharges": np.random.uniform(20.0, 8000.0, size=n_samples).astype(str),
    "Contract": np.random.choice(
        ["Month-to-month", "One year", "Two year"],
        size=n_samples,
        p=[0.5, 0.25, 0.25],
    ),
    "InternetService": np.random.choice(
        ["DSL", "Fiber optic", "No"], size=n_samples, p=[0.4, 0.4, 0.2]
    ),
    "Churn": np.random.choice(["No", "Yes"], size=n_samples, p=[0.73, 0.27]),
}

df = pd.DataFrame(data)

# Injecting some manual anomalies (Missing values & duplicates) for the cleaning steps
df.iloc[np.random.choice(n_samples, 15, replace=False), 3] = (
    " "  # Blanks in TotalCharges
)
df.iloc[np.random.choice(n_samples, 10, replace=False), 1] = np.nan  # NaN Tenure
df = pd.concat([df, df.iloc[:12]], ignore_index=True)  # Inject 12 duplicates

print("--- RAW DATA OVERVIEW ---")
print(f"Initial Shape: {df.shape}")
print(df.info(), "\n")


# ==========================================
# 2. DATA CLEANING & MISSING VALUES
# ==========================================
print("--- CLEANING DATA ---")

# Step A: Drop duplicate records
initial_rows = df.shape[0]
df = df.drop_duplicates()
print(f"Removed {initial_rows - df.shape[0]} duplicate rows.")

# Step B: Standardize numeric formatting and catch blank strings
df["TotalCharges"] = df["TotalCharges"].str.strip()
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Step C: Assess remaining missing values
print("\nMissing values before imputation:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Step D: Apply Median Imputation using NumPy & Pandas
tenure_median = df["Tenure"].median()
total_charges_median = df["TotalCharges"].median()

df["Tenure"] = df["Tenure"].fillna(tenure_median)
df["TotalCharges"] = df["TotalCharges"].fillna(total_charges_median)

print(f"\nImputed missing 'Tenure' with median: {tenure_median}")
print(f"Imputed missing 'TotalCharges' with median: {total_charges_median:.2f}")


# ==========================================
# 3. SUMMARY STATISTICS
# ==========================================
print("\n--- DESCRIPTIVE STATISTICS ---")
# Summary stats for numerical fields
print(df.describe().T)

# Summary stats for categorical values
print("\nCategorical Features Profile:")
print(df.describe(include=["object"]).T)

# Class balance check
churn_percentage = df["Churn"].value_counts(normalize=True) * 100
print(f"\nTarget Class Mix (Churn):\n{churn_percentage}")


# ==========================================
# 4. PATTERN RECOGNITION & VISUALIZATION
# ==========================================
# Define styling configurations
sns.set_theme(style="whitegrid", palette="muted")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Subplot 1: Overall target distribution balance
sns.countplot(ax=axes[0, 0], x="Churn", data=df)
axes[0, 0].set_title("Overall Retention vs Churn Class Proportions")
axes[0, 0].set_xlabel("Did the Customer Churn?")

# Subplot 2: Contract type behavioral correlations
sns.countplot(ax=axes[0, 1], x="Contract", hue="Churn", data=df)
axes[0, 1].set_title("Churn Incidents Segmented by Contract Commitment")
axes[0, 1].set_xlabel("Contract Type")

# Subplot 3: Financial distribution dynamics
sns.boxplot(ax=axes[1, 0], x="Churn", y="MonthlyCharges", data=df)
axes[1, 0].set_title(
    "Impact of Monthly Billing Rates on Customer Retention"
)
axes[1, 0].set_ylabel("Monthly Charge ($)")

# Subplot 4: Linear feature interactions (Correlation Map)
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(
    ax=axes[1, 1],
    data=numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    square=True,
)
axes[1, 1].set_title("Correlation Matrices Across Continuous Metrics")

plt.tight_layout()
plt.show()

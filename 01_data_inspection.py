
import pandas as pd


# Load the sales dataset
df = pd.read_csv(
    "data/superstore.csv",
    encoding="latin1"
)

# Display the first five rows
print("FIRST FIVE ROWS")
print(df.head())

# Display the dataset dimensions
print("\nDATASET SHAPE")
print(df.shape)

# Display column names and data types
print("\nDATASET INFORMATION")
df.info()

# Check for missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())


import pandas as pd

# Load the dataset
file_path = 'HIV&AIDS_Annual_Report_New_York.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Print the first few rows to check the data format
print(data.head())

# Remove rows where any column contains 'All' (since it's not useful for analysis)
data_cleaned = data[(data != 'All').all(axis=1)]

# Convert columns that should be numeric (like 'HIV diagnoses') to numeric
data_cleaned['HIV diagnoses'] = pd.to_numeric(data_cleaned['HIV diagnoses'], errors='coerce')

# Remove rows where 'HIV diagnoses' is NaN after conversion
data_cleaned = data_cleaned.dropna(subset=['HIV diagnoses'])

# Check for any non-numeric values in 'HIV diagnoses'
print(data_cleaned['HIV diagnoses'].dtype)  # It should print 'int64' or 'float64'

# Expand rows based on counts in 'HIV diagnoses' column
expanded_rows = []

for _, row in data_cleaned.iterrows():
    count = int(row['HIV diagnoses'])  # Use 'HIV diagnoses' as the count for row expansion
    for _ in range(count):
        expanded_rows.append(row)

# Convert the expanded rows to a new DataFrame
expanded_data = pd.DataFrame(expanded_rows)

# Save the expanded and cleaned data to a new CSV
expanded_data.to_csv('expanded_dataset.csv', index=False)

print("Data expanded and saved to 'expanded_dataset.csv'.")

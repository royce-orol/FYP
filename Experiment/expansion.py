import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/haziqzairul/Desktop/datafyp/Experiment/HIV&AIDS_Annual_Report_New_York.csv')

# Step 1: Filter rows where any categorical column contains "All"
categorical_columns = ['Year', 'Borough', 'UHF', 'Gender', 'Age', 'Race']
df = df[~df[categorical_columns].eq('All').any(axis=1)]

# Step 2: Handle missing values in relevant columns
df['HIV diagnoses'] = df['HIV diagnoses'].fillna(0).astype(int)
df['AIDS diagnoses'] = df['AIDS diagnoses'].fillna(0).astype(int)
df['% linked to care within 3 months'] = df['% linked to care within 3 months'].fillna(0).astype(float)

# Step 3: Expand rows for HIV and AIDS diagnoses
expanded_rows = []
for _, row in df.iterrows():
    num_hiv = row['HIV diagnoses']
    num_aids = row['AIDS diagnoses']
    pct_linked_to_care = row['% linked to care within 3 months'] / 100  # Convert percentage to decimal

    for i in range(num_hiv):
        new_row = row.copy()
        new_row['HIV_diagnosed'] = True
        new_row['AIDS_diagnosed'] = i < num_aids  # Assign True for the first `num_aids` rows
        new_row['Linked_to_care'] = i < round(num_hiv * pct_linked_to_care)  # Based on the percentage
        expanded_rows.append(new_row)

# Step 4: Create a new DataFrame with expanded rows
expanded_df = pd.DataFrame(expanded_rows)

# Step 5: Keep only necessary columns
expanded_df = expanded_df[['Year', 'Borough', 'UHF', 'Gender', 'Age', 'Race', 
                           'HIV_diagnosed', 'AIDS_diagnosed', 'Linked_to_care']]

# Step 6: Save the final expanded dataset
expanded_df.to_csv('/Users/haziqzairul/Desktop/datafyp/Experiment/expanded_dataset_with_linked_care.csv', index=False)

print(f"Final expanded row count: {len(expanded_df)}")

import numpy as np
import pandas as pd

# Load the dataset
file_path = 'Expanded_Individual_Data.csv'
data = pd.read_csv(file_path)

# Define the poverty level probabilities for 2020 and 2021
poverty_probs = {
    2020: {
        'Low Poverty (<10% below FPL)': {'HIV_diagnosed': 9.2, 'AIDS_diagnosed=True': 8.2, 'AIDS_diagnosed=False': 9.5},
        'Medium Poverty (10 to <20% below FPL)': {'HIV_diagnosed': 36.2, 'AIDS_diagnosed=True': 40.7, 'AIDS_diagnosed=False': 35.2},
        'High Poverty (20 to <30% below FPL)': {'HIV_diagnosed': 26.8, 'AIDS_diagnosed=True': 28.0, 'AIDS_diagnosed=False': 26.5},
        'Very High Poverty (>30% below FPL)': {'HIV_diagnosed': 20.6, 'AIDS_diagnosed=True': 17.5, 'AIDS_diagnosed=False': 21.3},
        'Unknown': {'HIV_diagnosed': 7.2, 'AIDS_diagnosed=True': 5.6, 'AIDS_diagnosed=False': 7.5}
    },
    2021: {
        'Low Poverty (<10% below FPL)': {'HIV_diagnosed': 12.2, 'AIDS_diagnosed=True': 16.6, 'AIDS_diagnosed=False': 11.2},
        'Medium Poverty (10 to <20% below FPL)': {'HIV_diagnosed': 34.7, 'AIDS_diagnosed=True': 31.9, 'AIDS_diagnosed=False': 11.2},
        'High Poverty (20 to <30% below FPL)': {'HIV_diagnosed': 23.7, 'AIDS_diagnosed=True': 28.0, 'AIDS_diagnosed=False': 22.6},
        'Very High Poverty (>30% below FPL)': {'HIV_diagnosed': 19.1, 'AIDS_diagnosed=True': 16.6, 'AIDS_diagnosed=False': 19.7},
        'Unknown': {'HIV_diagnosed': 10.4, 'AIDS_diagnosed=True': 6.8, 'AIDS_diagnosed=False': 11.2}
    },
    2019: {
        'Low Poverty (<10% below FPL)': {'HIV_diagnosed': 7.6, 'AIDS_diagnosed=True': 9.5, 'AIDS_diagnosed=False': 7.2},
        'Medium Poverty (10 to <20% below FPL)': {'HIV_diagnosed': 33.4, 'AIDS_diagnosed=True': 34.4, 'AIDS_diagnosed=False': 33.2},
        'High Poverty (20 to <30% below FPL)': {'HIV_diagnosed': 26.5, 'AIDS_diagnosed=True': 26.5, 'AIDS_diagnosed=False': 26.5},
        'Very High Poverty (>30% below FPL)': {'HIV_diagnosed': 23.4, 'AIDS_diagnosed=True': 23.8, 'AIDS_diagnosed=False': 23.3},
        'Unknown': {'HIV_diagnosed': 10.4, 'AIDS_diagnosed=True': 5.8, 'AIDS_diagnosed=False': 9.7}
      

    }
}


# Define the transmission category probabilities for 2020 and 2021
transmission_probs = {
    2020: {
        'MSM': {'HIV_diagnosed': 46.1, 'AIDS_diagnosed=True': 39.9, 'AIDS_diagnosed=False': 47.5},
        'IDU': {'HIV_diagnosed': 0.9, 'AIDS_diagnosed=True': 0.7, 'AIDS_diagnosed=False': 0.9},
        'MSM-IDU': {'HIV_diagnosed': 0.7, 'AIDS_diagnosed=True': 0.0, 'AIDS_diagnosed=False': 0.9},
        'Heterosexual Contact': {'HIV_diagnosed': 13.8, 'AIDS_diagnosed=True': 16.8, 'AIDS_diagnosed=False': 13.1},
        'TG-SC': {'HIV_diagnosed': 3.4, 'AIDS_diagnosed=True': 0.4, 'AIDS_diagnosed=False': 4.1},
        'Perinatal': {'HIV_diagnosed': 0.1, 'AIDS_diagnosed=True': 0.0, 'AIDS_diagnosed=False': 0.2},
        'Other': {'HIV_diagnosed': 0.0, 'AIDS_diagnosed=True': 0.0, 'AIDS_diagnosed=False': 0.0},
        'Unknown': {'HIV_diagnosed': 35.0, 'AIDS_diagnosed=True': 42.2, 'AIDS_diagnosed=False': 33.3}
    },
    2021: {
        'MSM': {'HIV_diagnosed': 46.9, 'AIDS_diagnosed=True': 38.1, 'AIDS_diagnosed=False': 49},
        'IDU': {'HIV_diagnosed': 0.9, 'AIDS_diagnosed=True': 0.3, 'AIDS_diagnosed=False': 1.1},
        'MSM-IDU': {'HIV_diagnosed': 1.3, 'AIDS_diagnosed=True': 0.3, 'AIDS_diagnosed=False': 1.6},
        'Heterosexual Contact': {'HIV_diagnosed': 14.8, 'AIDS_diagnosed=True': 19.2, 'AIDS_diagnosed=False': 13.8},
        'TG-SC': {'HIV_diagnosed': 3.6, 'AIDS_diagnosed=True': 1.0, 'AIDS_diagnosed=False': 4.2},
        'Perinatal': {'HIV_diagnosed': 0.1, 'AIDS_diagnosed=True': 0.3, 'AIDS_diagnosed=False': 0.1},
        'Other': {'HIV_diagnosed': 0, 'AIDS_diagnosed=True': 0, 'AIDS_diagnosed=False': 0},
        'Unknown': {'HIV_diagnosed': 32.3, 'AIDS_diagnosed=True': 40.7, 'AIDS_diagnosed=False': 33.3}
    },

    2019: {
        'MSM': {'HIV_diagnosed': 54, 'AIDS_diagnosed=True': 44.2, 'AIDS_diagnosed=False': 55.9},
        'IDU': {'HIV_diagnosed': 2, 'AIDS_diagnosed=True': 0.7, 'AIDS_diagnosed=False': 2.3},
        'MSM-IDU': {'HIV_diagnosed': 1.4, 'AIDS_diagnosed=True': 0.7, 'AIDS_diagnosed=False': 1.5},
        'Heterosexual Contact': {'HIV_diagnosed': 17.9, 'AIDS_diagnosed=True': 24.8, 'AIDS_diagnosed=False': 16.6},
        'TG-SC': {'HIV_diagnosed': 2.5, 'AIDS_diagnosed=True': 0.7, 'AIDS_diagnosed=False': 2.9},
        'Perinatal': {'HIV_diagnosed': 0.1, 'AIDS_diagnosed=True': 0.0, 'AIDS_diagnosed=False': 0.1},
        'Other': {'HIV_diagnosed': 0, 'AIDS_diagnosed=True': 0, 'AIDS_diagnosed=False': 0},
        'Unknown': {'HIV_diagnosed': 22.1, 'AIDS_diagnosed=True': 28.9, 'AIDS_diagnosed=False': 20.8}
    }

 }

linked_to_care_probs = {
    2019: {
        'Asian/Pacific Islander': 0.81,
        'Black': 0.80,
        'Latinx/Hispanic': 0.88,
        'White': 0.85
    },
    2020: {
        'Asian/Pacific Islander': 0.81,
        'Black': 0.77,
        'Latinx/Hispanic': 0.84,
        'White': 0.86
    },
    2021: {
        'Asian/Pacific Islander': 0.85,
        'Black': 0.79,
        'Latinx/Hispanic': 0.84,
        'White': 0.85
    }
}

# Define the probabilities for "% Viral Suppression"
viral_suppression_probs = {
    2019: {
        'Asian/Pacific Islander': 0.91,
        'Black': 0.79,
        'Latinx/Hispanic': 0.84,
        'White': 0.90
    },
    2020: {
        'Asian/Pacific Islander': 0.89,
        'Black': 0.79,
        'Latinx/Hispanic': 0.84,
        'White': 0.90
    },
    2021: {
        'Asian/Pacific Islander': 0.89,
        'Black': 0.79,
        'Latinx/Hispanic': 0.84,
        'White': 0.90
    }
}

def assign_viral_suppression(row):
    year = row['Year']
    race = row['Race']

    if year in viral_suppression_probs and race in viral_suppression_probs[year]:
        prob = viral_suppression_probs[year][race]
        return np.random.choice([True, False], p=[prob, 1 - prob])
    else:
        # If year or race is not found, return False by default
        return None


def assign_linked_to_care(row):
    year = row['Year']
    race = row['Race']

    if year in linked_to_care_probs and race in linked_to_care_probs[year]:
        prob = linked_to_care_probs[year][race]
        return np.random.choice([True, False], p=[prob, 1 - prob])
    else:
        # If year or race is not found, return False by default
        return None

# Function to assign Poverty Level
def assign_poverty_level(row):
    year = row['Year']
    aids_status = 'AIDS_diagnosed=True' if row['AIDS_diagnosed'] else 'AIDS_diagnosed=False'

    if year not in poverty_probs :
        print(f"Warning: Year {year} not found in either poverty_probs or transmission_probs. Skipping row.")
        return None  # Or assign a default category if needed

    # Get probabilities for the specified year and AIDS status
    probabilities = [
        poverty_probs[year]['Low Poverty (<10% below FPL)'][aids_status],
        poverty_probs[year]['Medium Poverty (10 to <20% below FPL)'][aids_status],
        poverty_probs[year]['High Poverty (20 to <30% below FPL)'][aids_status],
        poverty_probs[year]['Very High Poverty (>30% below FPL)'][aids_status],
        poverty_probs[year]['Unknown'][aids_status]
    ]
    
    # Normalize the probabilities
    total_prob = sum(probabilities)
    probabilities = [p / total_prob for p in probabilities]
    
    # Assign a poverty level
    poverty_level = np.random.choice(
        list(poverty_probs[year].keys()),
        p=probabilities
    )
    return poverty_level

# Function to assign Transmission Category
def assign_transmission_category(row):
    year = row['Year']
    aids_status = 'AIDS_diagnosed=True' if row['AIDS_diagnosed'] else 'AIDS_diagnosed=False'

    if year not in transmission_probs :
        print(f"Warning: Year {year} not found in either poverty_probs or transmission_probs. Skipping row.")
        return None  # Or assign a default category if needed

    # Get probabilities for the specified year and AIDS status
    probabilities = [
        transmission_probs[year]['MSM'][aids_status],
        transmission_probs[year]['IDU'][aids_status],
        transmission_probs[year]['MSM-IDU'][aids_status],
        transmission_probs[year]['Heterosexual Contact'][aids_status],
        transmission_probs[year]['TG-SC'][aids_status],
        transmission_probs[year]['Perinatal'][aids_status],
        transmission_probs[year]['Other'][aids_status],
        transmission_probs[year]['Unknown'][aids_status]
    ]

    # Exclude MSM and MSM-IDU for non-male genders
    if row['Gender'] != 'Male':
        probabilities[0] = 0  # MSM
        probabilities[2] = 0  # MSM-IDU
    
    # Exclude Perinatal for males
    if row['Gender'] == 'Male':
        probabilities[5] = 0  # Perinatal

    # Normalize the probabilities
    total_prob = sum(probabilities)
    probabilities = [p / total_prob for p in probabilities]

    # Assign a transmission category
    transmission_category = np.random.choice(
        list(transmission_probs[year].keys()),
        p=probabilities
    )
    return transmission_category

# Apply the functions to assign values
data['Poverty Level'] = data.apply(assign_poverty_level, axis=1)
data['Transmission Category'] = data.apply(assign_transmission_category, axis=1)
data['Linked to care within 3 months'] = data.apply(assign_linked_to_care, axis=1)
data['% Viral Suppression'] = data.apply(assign_viral_suppression, axis=1)



# Save the updated dataset
output_file_path = 'Updated_Expanded_Individual_Data.csv'
data.to_csv(output_file_path, index=False)

print(f"Dataset updated and saved to {output_file_path}")


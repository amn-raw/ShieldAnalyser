import pandas as pd
import numpy as np

# Create sample data for Faraday shield measurements
frequencies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
reference = [-20, -22, -21, -23, -24, -22, -25, -23, -24, -26, -25, -27]

# Generate sample location measurements (should be lower than reference for effective shielding)
np.random.seed(42)
l1_measurements = [ref - np.random.uniform(20, 30) for ref in reference]
l2_measurements = [ref - np.random.uniform(25, 35) for ref in reference]
l3_measurements = [ref - np.random.uniform(15, 25) for ref in reference]
l4_measurements = [ref - np.random.uniform(30, 40) for ref in reference]

# Create DataFrame
data = {
    'Frequency (MHz)': frequencies,
    'Reference': reference,
    'L1': l1_measurements,
    'L2': l2_measurements,
    'L3': l3_measurements,
    'L4': l4_measurements
}

df = pd.DataFrame(data)

# Round to 2 decimal places
df = df.round(2)

# Save to Excel
df.to_excel('sample_experiment.xlsx', index=False, sheet_name='Measurements')

print("Sample Excel file 'sample_experiment.xlsx' created successfully!")
print("\nPreview:")
print(df)


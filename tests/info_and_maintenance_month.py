import pandas as pd

# Load the maintenance schedule and services data
maintenance_df = pd.read_csv('data/maintenance_schedule_months.csv')
services_df = pd.read_csv('data/maintenance_services.csv')

# Create a mapping from symbols to actions
symbol_to_action = dict(zip(services_df['Symbol'], services_df['Action']))
print(symbol_to_action)

# Function to translate cell values based on the mapping
def translate_cell(cell):
    if pd.isna(cell):
        return cell
    for symbol, action in symbol_to_action.items():
        cell = str(cell).replace(symbol, action)
    return cell


# Get the columns that contain service information
service_columns = maintenance_df.columns.drop('Service') if 'Service' in maintenance_df.columns else maintenance_df.columns

# Apply the translation to the service columns
maintenance_df[service_columns] = maintenance_df[service_columns].applymap(
    translate_cell)

# Save the translated DataFrame to a new CSV file
maintenance_df.to_csv(
    'data/maintenance_schedule_months_translated.csv', index=False)

print(maintenance_df)

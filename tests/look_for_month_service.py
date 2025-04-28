import pandas as pd

df = pd.read_csv('data/maintenance_schedule_months.csv')

# look for every service in a month option
def find_service_month(month):
    if str(month) in df.columns:
        services = df.loc[:, ["Service", str(month)]]
        return services
    else:
        return "No services found for this months."

# Usage 
month = 12
services = find_service_month(month)

# Display the services
print(f"Services to be performed at {month} months:")
print(services.to_string(index=False))
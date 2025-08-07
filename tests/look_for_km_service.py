import pandas as pd

def find_service_km(km, df):
    if str(km) in df.columns:
        services = df.loc[:, ["Service", str(km)]]
        return services
    else:
        return "No services found for this km."

if __name__ == "__main__":
    km = 20
    df = pd.read_csv('data/maintenance_schedule_km_translated.csv')
    services = find_service_km(km, df)
    print(f"Services for {km} km:")
    print(services.to_string(index=False))
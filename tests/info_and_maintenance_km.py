import pandas as pd

# Carrega os CSVs
maintenance_df = pd.read_csv('data/maintenance_schedule_km.csv')
services_df = pd.read_csv('data/maintenance_services.csv')

# Constrói o dicionário correto de símbolo para ação
symbol_to_action = dict(zip(services_df['Symbol'], services_df['Action']))
print(symbol_to_action)

# Função para substituir dentro de cada célula
def translate_cell(cell):
    if pd.isna(cell):
        return cell
    for symbol, action in symbol_to_action.items():
        cell = cell.replace(symbol, action)
    return cell

# Protege a escolha das colunas
service_columns = maintenance_df.columns.drop('KM') if 'KM' in maintenance_df.columns else maintenance_df.columns

# Aplica a tradução apenas nas colunas de serviço
maintenance_df[service_columns] = maintenance_df[service_columns].applymap(translate_cell)

# Salva o resultado
maintenance_df.to_csv('data/maintenance_schedule_km_translated.csv', index=False)

print(maintenance_df)

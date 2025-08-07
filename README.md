# Assistente de Manutenção para Royal Enfield 🏍️

Um sistema inteligente para gerenciar e rastrear a manutenção de motocicletas Royal Enfield com base nos manuais oficiais da marca.

## 📋 Sobre o Projeto

Este projeto é um assistente de manutenção desenvolvido especificamente para motocicletas Royal Enfield. O sistema utiliza os dados oficiais de manutenção preventiva da marca para fornecer informações precisas sobre quando e quais serviços devem ser realizados, seja baseado em quilometragem ou tempo de uso.

### 🎯 Objetivos

- **Automação**: Facilitar o acompanhamento de manutenções preventivas
- **Organização**: Centralizar informações de manutenção em um local acessível
- **Eficiência**: Reduzir custos e aumentar a vida útil do veículo
- **Conformidade**: Seguir rigorosamente as especificações da Royal Enfield

## 🚀 Funcionalidades

### Versão Atual (MVP)

- ✅ Consulta de manutenções por quilometragem
- ✅ Consulta de manutenções por período (meses)
- ✅ Decodificação de símbolos de serviço (I, R, C, L, A)
- ✅ Base de dados completa de serviços de manutenção
- ✅ Scripts de teste e validação

### Funcionalidades Futuras

- 🔄 Interface gráfica (GUI) intuitiva
- 🔄 Banco de dados relacional (substituindo CSVs)
- 🔄 Sistema de notificações e lembretes
- 🔄 Histórico de manutenções realizadas
- 🔄 Relatórios de custos e estatísticas
- 🔄 Integração com calendário
- 🔄 Suporte multi-usuário
- 🔄 Backup automático de dados

## 📁 Estrutura do Projeto

```text
RE_maintenance_assistant/
├── data/                                    # Dados de manutenção
│   ├── maintenance_services.csv             # Códigos de serviços (I, R, C, L, A)
│   ├── maintenance_schedule_km.csv          # Cronograma por quilometragem (códigos)
│   ├── maintenance_schedule_km_translated.csv # Cronograma por quilometragem (texto)
│   ├── maintenance_schedule_months.csv      # Cronograma por meses (códigos)
│   └── maintenance_schedule_months_translated.csv # Cronograma por meses (texto)
├── notebooks/                              # Jupyter notebooks para análise
│   ├── df_maintenance_km_to_csv.ipynb      # Processamento dados km
│   ├── df_maintenance_months_to_csv.ipynb  # Processamento dados meses
│   └── df_service_opt_to_csv.ipynb         # Processamento códigos serviços
├── tests/                                  # Scripts de teste e validação
│   ├── info_and_maintenance_km.py          # Testes de consulta por km
│   ├── info_and_maintenance_month.py       # Testes de consulta por meses
│   ├── look_for_km_service.py              # Busca serviços por km
│   └── look_for_month_service.py           # Busca serviços por meses
└── README.md                               # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

### Versão Atual

- **Python 3.x**: Linguagem principal
- **Pandas**: Manipulação e análise de dados
- **CSV**: Armazenamento temporário de dados
- **Jupyter Notebook**: Análise e prototipagem

### Tecnologias Futuras

- **SQLite/PostgreSQL**: Banco de dados relacional
- **Flask**: Interface gráfica
- **SQLAlchemy**: ORM para banco de dados
- **Schedule**: Agendamento de tarefas
- **Pytest**: Testes automatizados

## 📊 Base de Dados

### Códigos de Serviço

| Símbolo | Ação                   |
| ------- | ---------------------- |
| **I**   | Inspect (Inspecionar)  |
| **R**   | Replace (Substituir)   |
| **C**   | Clean (Limpar)         |
| **L**   | Lubricate (Lubrificar) |
| **A**   | Adjust (Ajustar)       |

### Intervalos de Manutenção

- **Por Quilometragem**: 0.5k, 5k, 10k, 15k, 20k, 25k, 30k, 35k, 40k, 45k, 50k km
- **Por Tempo**: 1.5, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60 meses

## 🚦 Como Usar

### Pré-requisitos

```bash
# Instalar Python 3.x
# Instalar pandas
pip install pandas
```

### Executando os Testes

```bash
# Navegar até o diretório do projeto
cd RE_maintenance_assistant

# Executar consulta por quilometragem
python tests/look_for_km_service.py

# Executar consulta por meses
python tests/look_for_month_service.py

# Visualizar informações detalhadas
python tests/info_and_maintenance_km.py
python tests/info_and_maintenance_month.py
```

### Exemplo de Uso

```python
import pandas as pd

# Carregar dados de manutenção por km
df_km = pd.read_csv('data/maintenance_schedule_km_translated.csv')

# Consultar manutenções aos 10.000 km
maintenance_10k = df_km['10'].dropna()
print(maintenance_10k)
```

## 🔄 Roadmap de Desenvolvimento

### Fase 1: MVP (Atual) ✅

- [x] Estrutura básica de dados
- [x] Scripts de consulta
- [x] Validação dos dados
- [x] Documentação inicial

### Fase 2: Interface Gráfica 🔄

- [x] Design da interface do usuário
- [ ] Implementação com Flask
- [ ] Sistema de entrada de dados
- [ ] Visualização de resultados

### Fase 3: Banco de Dados 🔄

- [ ] Migração de CSV para SQLite
- [ ] Modelagem relacional
- [ ] APIs de acesso aos dados
- [ ] Sistema de backup

### Fase 4: Funcionalidades Avançadas 🔄

- [ ] Sistema de notificações
- [ ] Histórico de manutenções
- [ ] Relatórios e estatísticas
- [ ] Integração com calendário

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Para contribuir:

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. Abra um **Pull Request**

### Diretrizes de Contribuição

- Seguir PEP 8 para código Python
- Adicionar testes para novas funcionalidades
- Atualizar documentação quando necessário
- Usar mensagens de commit descritivas

## 📋 Requisitos do Sistema

### Requisitos Mínimos

- Python 3.7+
- 50MB de espaço em disco
- 512MB de RAM

### Requisitos Recomendados

- Python 3.9+
- 200MB de espaço em disco
- 1GB de RAM

## 👥 Autores

- **Vinicius Monnerat** - _Desenvolvedor Principal_ - [@viniciuscmb](https://github.com/viniciuscmb)

## 🙏 Agradecimentos

- **Royal Enfield** - Pelos manuais de manutenção oficiais
- **Comunidade Python** - Pelas ferramentas e bibliotecas
- **Motociclistas RE** - Por inspirar este projeto

## 📞 Contato

- **LinkedIn**: [Vinicius Monnerat](https://www.linkedin.com/in/vinicius-c-monnerat/)
- **GitHub**: [@viniciuscmb](https://github.com/viniciuscmb)

## 🔗 Links Úteis

- [Manuais Oficiais Royal Enfield](https://www.royalenfield.com/br/pt/support/owners-manual/)
- [Documentação Python](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

⚡ **Mantenha sua Royal Enfield sempre em perfeito estado!** ⚡
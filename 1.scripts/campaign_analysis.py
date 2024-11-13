print("Importing libraries...")
import pandas as pd
from functions import basic_etl

print("Loading database...")
# File directory and information
dir = "../0.bases"  # Directory
arq = "Planilha teste calculo e analises - Gabriella Maia"  # File name
sheet = "MEDIA DETAIL RESULTS"  # Sheet name
dir_saida = "../2.saidas"  # Output directory

# Loading the Excel file and sheet
df = pd.read_excel(f'{dir}/{arq}.xlsx', sheet_name=sheet, skiprows=10)

print("Applying basic ETL function...")
df = basic_etl(df)

print("Exporting cleaned database...")

# Exporting the cleaned DataFrame to a new CSV file
df.to_csv(f"{dir_saida}/cleaned_database.csv", index=False, encoding='utf-8')

print("Done! :)")


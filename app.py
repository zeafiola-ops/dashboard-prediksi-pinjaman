import pandas as pd

df = pd.read_excel("hasil_prediksi_deployment_google_sheets.xlsx")
print(df.columns.tolist())

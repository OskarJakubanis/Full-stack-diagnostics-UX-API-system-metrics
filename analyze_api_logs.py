import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych
df_logs = pd.read_csv("api_logs.csv", parse_dates=["timestamp"])

# Tabela błędów
error_codes = [400, 401, 403, 404, 429, 500, 503]
errors = df_logs[df_logs["status_code"].isin(error_codes)]

# Liczba błędów per endpoint
errors_by_endpoint = errors["endpoint"].value_counts()
print("Błędy per endpoint:\n", errors_by_endpoint)

# Średni czas odpowiedzi per service
avg_response = df_logs.groupby("service_name")["response_time_ms"].mean()
print("\nŚredni czas odpowiedzi (ms):\n", avg_response)

# Wykres statusów
plt.figure(figsize=(8, 4))
df_logs["status_code"].value_counts().sort_index().plot(kind="bar", color="skyblue")
plt.title("Rozkład statusów HTTP")
plt.xlabel("Status code")
plt.ylabel("Liczba wystąpień")
plt.tight_layout()
plt.savefig("api_status_codes.png")

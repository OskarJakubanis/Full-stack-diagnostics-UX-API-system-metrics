from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych (zakładam, że pliki są w katalogu roboczym)
logs_df = pd.read_csv('api_logs.csv')

# Analiza metryk
total_requests = len(logs_df)
error_requests = len(logs_df[logs_df['status_code'] >= 400])
error_rate = round((error_requests / total_requests) * 100, 2)
avg_response_time = round(logs_df['response_time_ms'].mean(), 2)
worst_service = logs_df.groupby('service_name')['response_time_ms'].mean().idxmax()

# Wykres błędów wg service_name
error_by_service = logs_df[logs_df['status_code'] >= 400].groupby('service_name').size()
plt.figure(figsize=(8, 4))
error_by_service.plot(kind='bar', color='tomato')
plt.title('Błędy HTTP wg Service')
plt.xlabel('Service')
plt.ylabel('Liczba błędów')
plt.tight_layout()
plt.savefig('errors_by_service.png')
plt.close()

# Generowanie raportu PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', size=12)
pdf.cell(200, 10, txt='Raport systemowy API - PDF', ln=True, align='C')

pdf.ln(10)
pdf.multi_cell(0, 10, txt=f'''
📊 Podsumowanie:
- Całkowita liczba żądań: {total_requests}
- Liczba błędów: {error_requests} ({error_rate}%)
- Średni czas odpowiedzi: {avg_response_time} ms
- Najwolniejsza usługa: {worst_service}
''')

pdf.ln(10)
pdf.cell(0, 10, txt='📉 Błędy wg Service:', ln=True)
pdf.image('errors_by_service.png', x=10, w=180)

pdf.output('system_api_report.pdf')

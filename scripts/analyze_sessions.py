import pandas as pd

# Wczytanie
df_sessions = pd.read_csv("session_tracking.csv", parse_dates=["start_time", "end_time"])

# Czas trwania sesji
df_sessions["duration_min"] = (df_sessions["end_time"] - df_sessions["start_time"]).dt.total_seconds() / 60

# Najczęstsze drop-offy
drop_offs = df_sessions["drop_off_page"].value_counts()
print("Najczęstsze drop-offy:\n", drop_offs)

# Średnia długość sesji
print("\nŚrednia długość sesji:", df_sessions["duration_min"].mean(), "min")

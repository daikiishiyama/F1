import fastf1
from fastf1 import plotting
import pandas as pd
import os
import matplotlib.pyplot as plt

# 🧠 Enable caching (downloads will be saved for future reuse)
fastf1.Cache.enable_cache('data/cache')  # Will create 'data/cache/' if it doesn't exist

# 📅 Load a specific session (e.g., 2024 Bahrain Grand Prix - Race)
year = 2024
event = 'Bahrain Grand Prix'
session_type = 'R'  # 'R' = Race, 'Q' = Qualifying, 'FP1', etc.

print(f"Loading {event} {session_type} session for {year}...")
session = fastf1.get_session(year, event, session_type)
session.load()

# 🏁 Get lap data
laps = session.laps
# Plot the lap data
plotting.setup_mpl(misc_mpl_mods=False)  # Setup matplotlib for FastF1
laps.plot(x='LapNumber', y='Speed', kind='line', title=f'{event} {year} - Lap Speeds', xlabel='Lap Number', ylabel='Speed (km/h)')
plt.tight_layout()
plt.show()
# Save lap data to CSV
laps.to_csv('data/laps_bahrain_2023.csv', index=False)
print("✅ Lap data saved to 'data/laps_bahrain_2023.csv'")

# 🚗 Get telemetry data for a specific driver (e.g., VER)
driver = 'VER'
ver_laps = laps.pick_driver(driver)
fastest_ver_lap = ver_laps.pick_fastest()
telemetry = fastest_ver_lap.get_car_data().add_distance()

# 📊 Plot telemetry speed over distance
plt.figure(figsize=(10, 5))
plt.plot(telemetry['Distance'], telemetry['Speed'], label='Speed (km/h)')
plt.title(f'{driver} – Fastest Lap Speed Profile – {event} {year}')
plt.xlabel('Distance (m)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

telemetry.to_csv(f'data/{driver}_telemetry_bahrain_2023.csv', index=False)
print(f"✅ Telemetry for {driver} saved to 'data/{driver}_telemetry_bahrain_2023.csv'")

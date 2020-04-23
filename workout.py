import ctypes  # An included library with Python install.   
import time
import sqlite3

# Save database initialize
conn = sqlite3.connect('workoutdata.db', isolation_level=None)
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS workoutdata (ID INTEGER PRIMARY KEY AUTOINCREMENT, part TEXT, type TEXT, minreps INTEGER, difficulty INTEGER, curReps REAL, overHeat INTEGER, totalAlerts INTEGER)')

while True:
    ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
    time.sleep(5)
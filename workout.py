import ctypes  # An included library with Python install.   
import time
import sqlite3
import random
import math
import os

PARTS = ['Upper', 'Lower', 'Torso', 'Core']
TYPE = ['Reps', 'Secs']

# Default workouts can not be deleted by the end user.
# Format: name TEXT, part TEXT, type TEXT, minreps(secs) INTEGER, difficulty INTEGER
default_workouts = [
    ['Pushup', PARTS[0], TYPE[0], 6, 2],
    ['Squat', PARTS[1], TYPE[0], 6, 2],
    ['Planche', PARTS[0], TYPE[1], 40, 4]
]
default_names = [workout[0] for workout in default_workouts]

print(default_names)

# Save database initialize
def createTable():
    # Create table and fill it with default workouts if it is empty
    cursor.execute('CREATE TABLE IF NOT EXISTS workoutdata (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, part TEXT, type TEXT, minreps INTEGER, difficulty INTEGER, curReps REAL, overHeat INTEGER, totalAlerts INTEGER)')

    for workout in default_workouts:
        cursor.execute('INSERT INTO workoutdata(name, part, type, minreps, difficulty, curReps, overHeat, totalAlerts) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', 
        (workout[0], workout[1], workout[2], workout[3], workout[4], workout[3], 0, 0))


if os.path.exists('workoutdata.db'):
    conn = sqlite3.connect('workoutdata.db', isolation_level=None)
    cursor = conn.cursor()
else:
    conn = sqlite3.connect('workoutdata.db', isolation_level=None)
    cursor = conn.cursor()
    createTable()


def retrieveData():
    cursor.execute('SELECT ID FROM workoutdata')
    return cursor.fetchall()

cursor.execute('SELECT * FROM workoutdata')
load_workout_tuple = cursor.fetchall()
load_workout = [list(tuples) for tuples in load_workout_tuple]

print(load_workout)

# Calculate Resting time
def calculateRest():
    return 2000

# Randomly generates number that points to a workout ID
def pickWorkout():
    return random.randrange(0, len(retrieveData()))

def calculateReps(row):
    row[8] += 1
    row[7] += 1
    print(row[5], row[7])
    repincrease = math.log(((10-row[5])/row[7]))/2.2
    print(row[1] + " += " + str(repincrease))
    if repincrease <= 0:
        return row
    else:
        row[6] += repincrease
        return row

# Show Alert
while True:
    # Randomly pick a workout
    workout_index = random.randrange(0, len(retrieveData()))

    # Show an alert
    #ctypes.windll.user32.MessageBoxW(0, math.floor(str(load_workout[workout_index][6])), str(load_workout[workout_index][1]), 1)
    ctypes.windll.user32.MessageBoxW(0, str(load_workout[workout_index][6]) + ", alert: " +str(load_workout[workout_index][7]), str(load_workout[workout_index][1]), 1)

    # Update Reps
    load_workout[workout_index] = calculateReps(load_workout[workout_index])

    # Apply to the database
    cursor.execute("UPDATE workoutdata SET curReps=?, totalAlerts=? WHERE ID=?", (load_workout[workout_index][6], load_workout[workout_index][8], load_workout[workout_index][0]))

    # Give the time to rest
    time.sleep(calculateRest())





from plyer import notification
import os.path
import time
import sqlite3
import random

# SAVE FILE MANAGEMENT
savefile = 'workout_save.txt'

# Default workout moves
excercises = ['Squat', 'Pull up', 'Dip', 'Reverse push-up', 'Reverse curl', 'Burpees' ,'ABS role', 'Planche']
excercise_reps = ['10' for excercise in excercises]

# Checking if the save file exists, if not, create one. If so, check if it is up to date with all the excercises.
if os.path.exists(savefile):
    with open(savefile, 'r') as f:
        for lines in f:
            print(lines)
else:
    with open(savefile, 'w') as f:
        f.write(','.join(excercises))
        f.write('\n')
        f.write(','.join(excercise_reps))



excercise_tuple = list(zip(excercises, excercise_reps))

def pickExcercise():
    # Returns excercise, and reps
    return excercise_tuple[random.randint(0, len(excercises)-1)][0], excercise_tuple[random.randint(0, len(excercises)-1)][1]

while True:
    name, reps = pickExcercise()
    notification.notify(
        title=name,
        message=str(reps),
        # app_icon='./icons/anime.ico',  # e.g. 'C:\\icon_32x32.ico'
        # timeout=2,  # seconds
    )
    time.sleep(2)



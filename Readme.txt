Workout notifier is a simple python script that reminds you to get up your ass and work out a bit.

It consists of a single python script that runs infinitely. On the first execution, it will create a .db database with three basic workout moves.

You can edit the 'workoutdata' table in the database to add your workout moves, just remember this format:

ID: Primary key, don't touch this.
name: The name of your workout. TEXT.
part, type: These do nothing as of current.
minreps: Minimum reps or seconds.
difficulty: The difficulty of the move. input integer value between 1 to 10. It affects reps/secs increase: higher the number, lower the increase.
curReps: Input the same value as minreps. Or any reps you want to do.
overHeat: Leave it as 0.
totalAlerts: This records how many times you've done the move.

There's no GUI, so the recommanded execution method of this script is to create a .bat file on Windows in the following format:
python SCRIPT PATH

The code is very simple and comes with comments, you'll be able to understand it easily.

Thank you for reading.


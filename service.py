import subprocess

independent_process = subprocess.Popen(
    'python D:\_Code\workout\Alert.py',
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
)
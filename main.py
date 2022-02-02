#importing
import subprocess
from flask_trials.trial_app import staying_alive
from exceptions import FileNotFound
#input the number of the file (example :
#flask trials/trial_app.py is 2 then 1)

folder = int(
    input("Enter the number of the folder (example: flask trials is 1): "))

print(folder)
if folder == 1:
    file = int(input("Enter the number of the file: "))
    if file == 1:
      staying_alive()
      subprocess.Popen(["python","flask_trials/trial_app.py"])
      print(file)
    else:
      raise FileNotFound("The folder is not found.")
else:
  raise FileNotFound("The folder is not found.")
    


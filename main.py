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
    print(file)
    if file == 1:
      sure=input("Are you sure to start this project?(y/n)")
      print(sure)
      if sure == "y":
        subprocess.Popen(["python","flask_trials/trial_app.py"])
        staying_alive()
      else:
        exit()
    else:
      raise FileNotFound("The file is not found.")
else:
  raise FileNotFound("The folder is not found.")
    


#importing
import subprocess
from flask_trials.trial_app import staying_alive, run
from exceptions import FileNotFound, WrongAnswer
#input the number of the file (example :
#flask trials/trial_app.py is 1.)
folder =input("Enter the number of the folder (example: flask trials is 1): ")

print(folder)
if folder == '1':
    file = input("Enter the number of the file: ")
    print(file)
    if file == '1':
      sure=input("Are you sure to start this project?(y/n): ")
      print(sure)
      if sure == "y":
        subprocess.Popen(["python","flask_trials/trial_app.py"])
        run()
        staying_alive()
      elif sure == 'n':
        print("Ok, goodbye!")
        exit()
      else:
        raise WrongAnswer("You need to answer with y or n.")
    else:
      raise FileNotFound("The file is not found.")
else:
  raise FileNotFound("The folder is not found.")
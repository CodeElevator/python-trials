#importing
import subprocess
from flask_trials.trial_app import staying_alive
#input the number of the file (example :
#flask trials/trial_app.py is 2 then 1)
class FileNotFound(Exception):
  '''
  Custom exception for not finding the number of the file entered
  '''
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
    def __str__(self):
      print("calling str")
      if self.message:
        return 'FileNotFound, {0}'.format(self.message)
      else:
        return "FileNotFound has been raised"

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

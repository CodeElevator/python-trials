class FileNotFound(FileNotFoundError):
  '''
  Custom exception for not finding the number of the file entered.
  '''
  def __init__(self, *args):
    if args:
      self.message = args[0]
    else:
      self.message = None
    def __str__(self):
      if self.message:
        return 'FileNotFound, {0}'.format(self.message)
      else:
        return "FileNotFound, the file or the folder you entered is not found."

class WrongAnswer(Exception):
  '''
  Custom Error for the wrong answer in input.
  '''
  def __init__(self,*args):
    if args:
      self.message = args[0]
    else:
      self.message = None
  def __str__(self):
    if self.message:
      return 'WrongAnswer, {0}'.format(self.message)
    else:
      return "WrongAnswer, you need to put the good answer for this message."
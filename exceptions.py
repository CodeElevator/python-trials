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

#this is a flask webapp example
from flask import Flask
from threading import Thread
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

def staying_alive():
  '''
  Staying alive
  '''
  t=Thread(target="run")
  t.start()
def run():
  app.run(host='0.0.0.0', port=8080)
'''
  Author: Justin Clayton
'''

from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)

# Routes for app here
@app.route('/')
def index():
  return render_template('index.html')

if (__name__ == '__main__'):
  app.run(debug=True)

"""from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Set the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded files
    template_files = request.files.getlist('templateFiles')

    # Check if any files were uploaded
    if not template_files:
        return 'No template files uploaded'

    # Iterate over each uploaded file
    for template_file in template_files:
        if template_file.filename != '':
            # Save the file
            template_file.save(os.path.join(app.config['UPLOAD_FOLDER'], template_file.filename))

    return 'Template files uploaded successfully.'

if __name__ == '__main__':
    app.run(debug=True)"""
import sys
import os
from flask import Flask, render_template, request, jsonify
import pdf_reader as pr
import os 
import pandas as pd 
import txt_parser as tp
import numpy as np

# Flask application
app = Flask(__name__, template_folder='templates')
# Set the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
  os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
  # Get the uploaded files
  template_files = request.files.getlist('templateFiles')

  # Check if any files were uploaded
  if not template_files:
    return jsonify({'message': 'No template files uploaded'}), 400

  # Iterate over each uploaded file
  for template_file in template_files:
    if template_file.filename != '':
      # Save the file
      template_file.save(os.path.join(app.config['UPLOAD_FOLDER'], template_file.filename))

  # Run main.py 
  exec(open('main_code.py').read())

  return jsonify({'message': 'Template files uploaded successfully.'})

if __name__ == '__main__':
  app.run(debug=False)  # Run Flask app as a standalone server
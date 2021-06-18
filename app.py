# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:58:54 2021

@author: samuel
"""
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from glob import glob
import pickle
from model import search_frames, split_to_frames

UPLOAD_FOLDER = 'static/video_frames'
import os
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def index():
    return render_template('index.html')
@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
      f = request.files['videoInput']
      f.save(secure_filename(f.filename))
      
@app.route('/search', methods=['GET', 'POST'])

def search():
    # getting input with name = fname in HTML form
    search_text = request.form.get("searchInput")
    list_frames =  search_frames(search_text)
    #video = os.listdir('static/video_frames')
    return render_template('search.html', frames_list=list_frames)
		
if __name__ == '__main__':
    app.run(host='localhost', debug=True)
    app.run(host='localhost', debug=True)

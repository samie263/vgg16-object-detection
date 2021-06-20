# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:58:54 2021

@author: samuel
"""

from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
from model import search_frames, video_to_frames
import os
import json

UPLOAD_FOLDER = 'uploads/'

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=["GET"])
def index():
    with open('detected_objects.txt', 'r') as f:
        obj_nam = set(json.loads(f.read()))
    return render_template('index.html', obj_names=obj_nam)

@app.route('/', methods=["POST"])
def upload():
    if request.method == 'POST':
        file = request.files['videoInput']
        filename = secure_filename(file.filename)
        #os.mkdir('uploads', 777)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        video_to_frames(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #os.remove("uploads")
        flash('File(s) successfully uploaded')
        return redirect('/')
    

        
           
@app.route('/search', methods=['GET', 'POST'])
def search():
    # getting input with name = fname in HTML form
    search_text = request.form.get("searchInput")
    objects = search_frames(search_text)
    #video = os.listdir('static/video_frames')
    return render_template('search.html', frames_list=objects, search_txt=search_text)
		
if __name__ == '__main__':
    app.run(port=5002, debug=True)

